import argparse
import os
from pathlib import Path

from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from dotenv import load_dotenv


def _build_client() -> DocumentIntelligenceClient:
    """Create a Document Intelligence client using env vars."""
    load_dotenv()
    endpoint = os.getenv("AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT")
    api_key = os.getenv("AZURE_DOCUMENT_INTELLIGENCE_API_KEY")

    if not endpoint or not api_key:
        raise SystemExit(
            "AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT and "
            "AZURE_DOCUMENT_INTELLIGENCE_API_KEY must be set"
        )

    return DocumentIntelligenceClient(endpoint, AzureKeyCredential(api_key))


def _convert_pdf_to_markdown(client: DocumentIntelligenceClient, pdf_path: Path) -> str:
    """Send the PDF to Azure Document Intelligence and return markdown content."""
    with pdf_path.open("rb") as source:
        poller = client.begin_analyze_document(
            "prebuilt-layout",
            body=source,
            content_type="application/octet-stream",
            output_content_format="MARKDOWN",
        )
    result = poller.result()
    return result.content or ""


def _write_output(markdown: str, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown, encoding="utf-8")


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert a PDF to Markdown text with Azure Document Intelligence",
    )
    parser.add_argument(
        "-i", "--input", required=True, help="Path to the input PDF file"
    )
    parser.add_argument(
        "-o",
        "--output",
        required=True,
        help="Path to write the extracted markdown text",
    )
    return parser.parse_args(argv)


def cli_main(argv: list[str] | None = None) -> None:
    args = _parse_args(argv)
    pdf_path = Path(args.input).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()

    if not pdf_path.exists():
        raise SystemExit(f"Input file not found: {pdf_path}")

    client = _build_client()
    markdown = _convert_pdf_to_markdown(client, pdf_path)
    _write_output(markdown, output_path)


if __name__ == "__main__":
    cli_main()
