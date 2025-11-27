# Azure によって直接販売される Foundry Models

O
Note

このドキュメントでは、Microsoft Foundry(クラシック) ポータルを参照します。

この記事では、Azure によって直接販売される Microsoft Foundry モデルの一覧と、その機能、デプロイの種類、および可用性のリージョン(
非推奨モデルとレガシ モデルを除く)を示します。 Foundry Agent Service でサポートされている Azure OpenAl モデルの一覧については、「エ
ージェント サービスでサポートされるモデル」を参照してください。

Azureによって直接販売されるモデルには、すべてのAzure OpenAIモデルと、上位プロバイダーから選択された特定のモデルが含まれます。

Microsoft Foundry で使用する プロジェクトの種類 に応じて、さまざまなモデルの選択が表示されます。具体的には、Foundry リソースに基づ
いて構築された Foundry プロジェクトを使用すると、Foundry リソースへの標準デプロイに使用できるモデルが表示されます。または、
Foundry ハブによってホストされているハブ ベースのプロジェクトを使用する場合は、マネージド コンピューティング API とサーバーレス API
へのデプロイに使用できるモデルが表示されます。多くのモデルで複数のデプロイ オプションがサポートされているため、これらのモデルの
選択肢は重複することがよくあります。

Azure によって直接販売される Foundry モデルの属性の詳細については、「 Foundry モデルの探索」を参照してください。

O
Note

Azure によって直接販売される Foundry Models には、次の上位モデル プロバイダーから選択したモデルも含まれます。

· ブラック フォレスト ラボ: FLUX.1-Kontext-pro、FLUX-1.1-pro

· DeepSeek: DeepSeek-V3.1 . DeepSeek-V3-0324 . DeepSeek-R1-0528 . DeepSeek-R1

● メタ: Llama-4-Maverick-17B-128E-Instruct-FP8、 Llama-3.3-70B-Instruct

· Microsoft: MAI-DS-R1

· ミストラル: mistral-document-ai-2505

. xAl: grok-code-fast-1, grok-3, grok-3-mini , grok-4-fast-reasoning . grok-4-fast-non-reasoning . grok-4

これらのモデルの詳細については、この記事の上部にある 他のモデル コレクション に切り替えます。


## Microsoft FoundryモデルのAzure OpenAI

Azure OpenAl は、さまざまな機能と価格ポイントを備えた多様なモデルセットを利用しています。 モデルの可用性はリージョンとクラウドご
とに異なります。Azure Government モデルの可用性については、「Azure Government の Azure OpenAl」を参照してください。

に テーブルを展開する


<table>
<tr>
<th>Models</th>
<th>Description</th>
</tr>
<tr>
<td>GPT-5.1 シリーズ</td>
<td>NEW gpt-5.1. gpt-5.1-chat, gpt-5.1-codex, gpt-5.1-codex-mini</td>
</tr>
<tr>
<td>そら</td>
<td>NEW sora-2</td>
</tr>
<tr>
<td>GPT-5 シリーズ</td>
<td>gpt-5, gpt-5-mini, gpt-5-nano. gpt-5-chat</td>
</tr>
<tr>
<td>gpt-oss</td>
<td>オープンウェイト推論モデル</td>
</tr>
<tr>
<td>codex-mini</td>
<td>o4-miniの微調整されたバージョン。</td>
</tr>
<tr>
<td>GPT-4.1 シリーズ</td>
<td>gpt-4.1. gpt-4.1-mini, gpt-4.1-nano</td>
</tr>
<tr>
<td>model-router</td>
<td>特定のプロンプトに応答するために、基になる一連のチャット モデルからインテリジェントに選択するモデル。</td>
</tr>
<tr>
<td>computer-use-preview</td>
<td>Responses API コンピューター使用ツールで使用するためにトレーニングされた実験モデル。</td>
</tr>
<tr>
<td>○ シリーズ モデル</td>
<td>高度な問題解決とフォーカスと能力の向上を備えた推論モデル。</td>
</tr>
<tr>
<td>GPT-40, GPT-40 mini, GPT-4 Turbo</td>
<td>マルチモーダル バージョンの対応 Azure OpenAl モデル。テキストと画像の両方を入力として受け入れることが可能です。</td>
</tr>
<tr>
<td>GPT-4</td>
<td>GPT-3.5 を基に改善され、自然言語とコードを理解し、生成できるモデルのセット。</td>
</tr>
<tr>
<td>GPT-3.5</td>
<td>GPT-3 を基に改善され、自然言語とコードを理解し、生成できるモデルのセット。</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th>Models</th>
<th>Description</th>
</tr>
<tr>
<td>Embeddings</td>
<td>テキストを数値ベクトル形式に変換して、テキストの類似性を促進できるモデルのセット。</td>
</tr>
<tr>
<td>イメージの生成</td>
<td>自然言語からオリジナルの画像を生成できるモデルのシリーズ。</td>
</tr>
<tr>
<td>Video generation</td>
<td>テキスト命令から元のビデオ シーンを生成できるモデル。</td>
</tr>
<tr>
<td>オーディオ</td>
<td>音声テキスト変換、翻訳、およびテキスト読み上げのための一連のモデル。GPT-40 オーディオ モデルでは、低待機時間 の音声イ ン、音声アウトの会話操作、またはオーディオ生成がサポートされます。</td>
</tr>
</table>


## GPT-5.1 リージョンの可用性

〔〕 テーブルを展開する


<table>
<tr>
<td>モデル</td>
<td>リージョン</td>
</tr>
<tr>
<td>gpt-5.1</td>
<td>米国東部 2 およびスウェーデン中部(グローバル標準および DataZone 標準)</td>
</tr>
<tr>
<td>gpt-5.1-chat</td>
<td>米国東部 2 およびスウェーデン中部(グローバル標準)</td>
</tr>
<tr>
<td>gpt-5.1-codex</td>
<td>米国東部 2 およびスウェーデン中部(グローバル標準)</td>
</tr>
<tr>
<td>gpt-5.1-codex-mini</td>
<td>米国東部2 およびスウェーデン中部(グローバル標準)</td>
</tr>
</table>

● gpt-5.1 および gpt-5.1-codex へのアクセスには登録が必要です 。


アクセスは、Microsoft の資格条件に基づいて付与されます。以前に制限付きアクセス モデルへのアクセスを適用して受け取ったお客様は、承
認されたサブスクリプションがモデルのリリース時に自動的にアクセス権を付与されるため、再適用する必要はありません。

〔〕 テーブルを展開する


<table>
<tr>
<th>モデル ID</th>
<th>Description</th>
<th>コンテキスト ウィンド ウ</th>
<th>最大出力トークン 数</th>
<th>トレーニング データ(最 大)</th>
</tr>
<tr>
<td rowspan="3">gpt-5.1 (2025-11-13)</td>
<td>- 推論 - Chat Completions APlo</td>
<td>400,000</td>
<td>128,000</td>
<td>2024 年9月30日</td>
</tr>
<tr>
<td rowspan="2">- 応答 API。 - 構造化出力 - テキストと画像処理。 - 関数、ツール、および並列ツール呼び出し。 - 機能の完全な概要。</td>
<td>入力:272,000</td>
<td rowspan="2"></td>
<td rowspan="2"></td>
</tr>
<tr>
<td>出力:128,000</td>
</tr>
<tr>
<td rowspan="4">gpt-5.1-chat (2025-11-13)</td>
<td>- 推論</td>
<td>128,000</td>
<td rowspan="2">16,384</td>
<td rowspan="4">2024 年 9月30日</td>
</tr>
<tr>
<td>- Chat Completions API.</td>
<td></td>
</tr>
<tr>
<td>- 応答 API。</td>
<td>入力:111,616</td>
<td rowspan="2"></td>
</tr>
<tr>
<td>- 構造化された出力 - 関数、ツール、および並列ツール呼び出し。</td>
<td>出力:16,384</td>
</tr>
<tr>
<td rowspan="2">gpt-5.1-codex (2025-11-13)</td>
<td>- 応答 API のみ。 - テキストと画像処理</td>
<td>400,000</td>
<td>128,000</td>
<td rowspan="2">2024 年9月30日</td>
</tr>
<tr>
<td>- 構造化出力 - 関数、ツール、および並列ツール呼び出し。 - 機能の完全な概要 - Codex CLI および Codex VS Code 拡張機能用に最 適化</td>
<td>入力:272,000 出力:128,000</td>
<td></td>
</tr>
<tr>
<td rowspan="2">gpt-5.1-codex-mini (2025-11- 13)</td>
<td>- 応答 API のみ。 - テキストと画像処理</td>
<td>400,000</td>
<td>128,000</td>
<td>2024 年9月30日</td>
</tr>
<tr>
<td>- 構造化出力 - テキストと画像処理。 - 関数、ツール、および並列ツール呼び出し。 - 機能の完全な概要 - Codex CLI および Codex VS Code 拡張機能用に最 適化</td>
<td>入力:272,000 出力:128,000</td>
<td></td>
<td></td>
</tr>
</table>


<!-- PageFooter="1 重要" -->
<!-- PageBreak -->

● gpt-5.1 reasoning_effort は既定で none に設定されます。以前の推論モデルから gpt-5.1 にアップグレードする場合は、推論を実行
する場合は、 reasoning_effort レベルを明示的に渡すようにコードを更新する必要がある場合があることに注意してください。

● gpt-5.1-chat は、組み込みの推論機能を追加します。他の 推論モデル と同様に、temperature などのパラメーターはサポートされま
せん。 gpt-5-chat (推論モデルではない) を使用して gpt-5.1-chat アップグレードする場合は、推論モデルでサポートされていない
temperature などのカスタム パラメーターをコードから削除してください。


## GPT-5 リージョンの可用性

〔〕 テーブルを展開する


<table>
<tr>
<th>モデル</th>
<th>リージョン</th>
</tr>
<tr>
<td>gpt-5 (2025-08-07)</td>
<td>「モデル テーブル」を参照してください。</td>
</tr>
<tr>
<td>gpt-5-mini (2025-08-07)</td>
<td>「モデル テーブル」を参照してください。</td>
</tr>
<tr>
<td>gpt-5-nano (2025-08-07)</td>
<td>「モデル テーブル」を参照してください。</td>
</tr>
<tr>
<td>gpt-5-chat (2025-08-07)</td>
<td>「モデル テーブル」を参照してください。</td>
</tr>
<tr>
<td>gpt-5-chat (2025-10-03)</td>
<td>米国東部2 (グローバル標準) とスウェーデン中部(グローバル標準)</td>
</tr>
<tr>
<td>gpt-5-codex (2025-09-11)</td>
<td>米国東部2 (グローバル標準) とスウェーデン中部(グローバル標準)</td>
</tr>
<tr>
<td>gpt-5-pro (2025-10-06)</td>
<td>米国東部2(グローバル標準) とスウェーデン中部(グローバル標準)</td>
</tr>
</table>


● gpt-5-pro、gpt-5、および gpt-5-codex モデルへのアクセスには登録が必要です 。

● gpt-5-mini、gpt-5-nano、gpt-5-chat は登録を必要としません。

アクセスは、Microsoft の資格条件に基づいて付与されます。以前に 03 へのアクセスを適用して受け取ったお客様は、承認されたサブスクリプ
ションにモデルのリリース時に自動的にアクセス権が付与されるため、再適用する必要はありません。

〔〕 テーブルを展開する


<table>
<tr>
<th>モデル ID</th>
<th>Description</th>
<th>コンテキスト ウィンド ウ</th>
<th>最大出力トークン 数</th>
<th>トレーニング データ(最 大)</th>
</tr>
<tr>
<td rowspan="6">gpt-5 (2025-08-07)</td>
<td>- 推論</td>
<td>400,000</td>
<td>128,000</td>
<td>2024 年 9月30日</td>
</tr>
<tr>
<td>- Chat Completions API.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>- 応答 API。</td>
<td>入力:272,000</td>
<td rowspan="4"></td>
<td></td>
</tr>
<tr>
<td>- 構造化出力</td>
<td>出力:128,000</td>
<td rowspan="3"></td>
</tr>
<tr>
<td>- テキストと画像処理。 - 関数、ツール、および並列ツール呼び出し。</td>
<td></td>
</tr>
<tr>
<td>- 機能の完全な概要。</td>
<td></td>
</tr>
<tr>
<td rowspan="6">gpt-5-mini (2025-08-07)</td>
<td>- 推論</td>
<td>400,000</td>
<td>128,000</td>
<td rowspan="2">2024 年5月31日</td>
</tr>
<tr>
<td>- Chat Completions API.</td>
<td></td>
<td></td>
</tr>
<tr>
<td>- 応答 API。</td>
<td>入力:272,000</td>
<td rowspan="4"></td>
<td></td>
</tr>
<tr>
<td>- 構造化出力</td>
<td>出力:128,000</td>
<td rowspan="3"></td>
</tr>
<tr>
<td>- テキストと画像処理。 - 関数、ツール、および並列ツール呼び出し。</td>
<td></td>
</tr>
<tr>
<td>- 機能の完全な概要。</td>
<td></td>
</tr>
<tr>
<td rowspan="6">gpt-5-nano (2025-08-07)</td>
<td>- 推論</td>
<td>400,000</td>
<td>128,000</td>
<td rowspan="2">2024 年5月31日</td>
</tr>
<tr>
<td>- Chat Completions API.</td>
<td></td>
<td></td>
</tr>
<tr>
<td>- 応答 API。</td>
<td>入力:272,000</td>
<td rowspan="4"></td>
<td></td>
</tr>
<tr>
<td>- 構造化出力</td>
<td>出力:128,000</td>
<td rowspan="3"></td>
</tr>
<tr>
<td>- テキストと画像処理。 - 関数、ツール、および並列ツール呼び出し。</td>
<td rowspan="2"></td>
</tr>
<tr>
<td>- 機能の完全な概要。</td>
</tr>
<tr>
<td>gpt-5-chat (2025-08-07)</td>
<td>- Chat Completions API.</td>
<td>128,000</td>
<td>16,384</td>
<td>2024 年9月30日</td>
</tr>
<tr>
<td>プレビュー</td>
<td>- 応答 API。 - 入力: テキスト/画像 - 出力: テキストのみ</td>
<td></td>
<td></td>
<td></td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th>モデル ID</th>
<th>Description</th>
<th>コンテキスト ウィンド ウ</th>
<th>最大出カトークン 数</th>
<th>トレーニング データ(最 大)</th>
</tr>
<tr>
<td rowspan="4">gpt-5-chat (2025-10-03) プレビュー1</td>
<td>- Chat Completions API.</td>
<td>128,000</td>
<td>16,384</td>
<td rowspan="4">2024 年9月30日</td>
</tr>
<tr>
<td>- 応答 API。</td>
<td></td>
<td rowspan="3"></td>
</tr>
<tr>
<td>- 入力: テキスト/画像</td>
<td></td>
</tr>
<tr>
<td>- 出力: テキストのみ</td>
<td></td>
</tr>
<tr>
<td>gpt-5-codex (2025-09-</td>
<td>- 応答 API のみ。</td>
<td>400,000</td>
<td>128,000</td>
<td>-</td>
</tr>
<tr>
<td rowspan="5">11)</td>
<td>- 入力: テキスト/画像</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>- 出力: テキストのみ</td>
<td>入力:272,000</td>
<td rowspan="4"></td>
<td rowspan="4"></td>
</tr>
<tr>
<td>- 構造化出力</td>
<td>出力:128,000</td>
</tr>
<tr>
<td>- テキストと画像処理。 - 関数、ツール、および並列ツール呼び出し。 - 機能の完全な概要 - Codex CLI および Codex VS Code 拡張機能用に最適</td>
<td></td>
</tr>
<tr>
<td>化</td>
<td></td>
</tr>
<tr>
<td rowspan="6">gpt-5-pro (2025-10-06)</td>
<td>- 推論</td>
<td>400,000</td>
<td rowspan="2">128,000</td>
<td rowspan="2">2024 年9月30日</td>
</tr>
<tr>
<td>- 応答 API。</td>
<td></td>
</tr>
<tr>
<td>- 構造化出力</td>
<td>入力:272,000</td>
<td></td>
<td></td>
</tr>
<tr>
<td>- テキストと画像処理。</td>
<td>出力:128,000</td>
<td rowspan="3"></td>
<td rowspan="3"></td>
</tr>
<tr>
<td>- 関数とツール</td>
<td></td>
</tr>
<tr>
<td>- 機能の完全な概要。</td>
<td></td>
</tr>
</table>


### 1 Note

1gpt-5-chat バージョン 2025-10-03 は、感情的な知性と精神的健康能力に焦点を当てた重要な強化を導入します。このアップグレードで
は、特殊なデータセットと調整された応答戦略が統合され、モデルの次の機能が向上します。

● 感情コンテキストをより正確に理解して解釈し、微妙で共感的な相互作用を可能にします。

● メンタルヘルスに関連する会話では、支援的で責任ある対応を行い、感受性と最高の実践に従うことを確保します。

これらの改善により、GPT-5 チャットは、感情的なトーンと幸福に関する考慮事項が重要なシナリオで、コンテキストに対応し、人間中心
で信頼性が高くなります。


## gpt-oss リージョンの可用性

〔〕 テーブルを展開する


<table>
<tr>
<td>モデル</td>
<td>リージョン</td>
</tr>
<tr>
<td>gpt-oss-120b</td>
<td>すべてのAzure OpenAIリージョン</td>
</tr>
</table>


## 能力

こ〕 テーブルを展開する


<table>
<tr>
<th>モデル ID</th>
<th>Description</th>
<th>コンテキスト ウィン ドウ</th>
<th>最大出力トークン 数</th>
<th>トレーニング データ (最大)</th>
</tr>
<tr>
<td>gpt-oss-120b (プレビ ユー)</td>
<td>- テキストイン/テキストアウトのみ - チャット完了API -ストリーミング - 関数呼び出し - 構造化された出力 - 推論 - デプロイ1 およびマネージド コンピューティングを使用して使 用できます</td>
<td>131,072</td>
<td>131,072</td>
<td>2024 年5月31日</td>
</tr>
<tr>
<td>gpt-oss-20b (プレビュ ) ー</td>
<td>- テキストイン/テキストアウトのみ - チャット完了API -ストリーミング - 関数呼び出し - 構造化された出力</td>
<td>131,072</td>
<td>131,072</td>
<td>2024 年5月31日</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th>モデル ID</th>
<th>Description</th>
<th>コンテキスト ウィン ドウ</th>
<th>最大出力トークン 数</th>
<th>トレーニング データ (最大)</th>
</tr>
<tr>
<td colspan="5">- 推論 - マネージド コンピューティングと Foundry Local を介して使用 可能</td>
</tr>
</table>


1他のAzure OpenAIモデルとは異なり、gpt-oss-120bモデルをデプロイするにはFoundryプロジェクトが必要です。


## コードを使用してデプロイする

cli

az cognitiveservices account deployment create \
-- name "Foundry-project-resource" \
-- resource-group "test-rg" \
-- deployment-name "gpt-oss-120b" \
-- model-name "gpt-oss-120b" |
-- model-version "1" |
-- model-format "OpenAI-OSS" \
-- sku-capacity 10 \
-- sku-name "GlobalStandard"


# GPT-4.1 シリーズ


## リージョンの可用性

こ テーブルを展開する


<table>
<tr>
<th>モデル</th>
<th>リージョン</th>
</tr>
<tr>
<td>gpt-4.1 (2025-04-14)</td>
<td>「モデル テーブル」を参照してください。</td>
</tr>
<tr>
<td>gpt-4.1-nano (2025-04-14)</td>
<td>「モデル テーブル」を参照してください。</td>
</tr>
<tr>
<td>gpt-4.1-mini (2025-04-14)</td>
<td>「モデル テーブル」を参照してください。</td>
</tr>
</table>


# 能力


## 1 重要

既知の問題は、すべての GPT 4.1 シリーズ モデルに影響します。300,000 トークンを超える大規模なツールまたは関数呼び出しの定義で
は、モデルの 100 万個のトークン コンテキスト制限に達しなかった場合でも、エラーが発生します。

エラーは、API 呼び出しと基になるペイロードの特性によって異なる場合があります。

Chat Completions API のエラー メッセージを次に示します:

. Error code: 400 - {'error': {'message' : "This model's maximum context length is 300000 tokens. However, your messages resulted
in 350564 tokens (100 in the messages, 350464 in the functions). Please reduce the length of the messages or functions.",
'type' : 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded' } }

. Error code: 400 - {'error': {'message' : "Invalid 'tools[0]. function. description' : string too long. Expected a string with
maximum length 1048576, but got a string with length 2778531 instead.", 'type': 'invalid_request_error', 'param' :
'tools[0].function.description', 'code': 'string_above_max_length' } }

Responses API のエラー メッセージを次に示します:

. Error code: 500 - {'error': {'message' : 'The server had an error processing your request. Sorry about that! You can retry your
request, or contact us through an Azure support request at: https://go.microsoft.com/fwlink/?linkid=2213926 if you keep seeing
this error. (Please include the request ID d2008353-291d-428f-adc1-defb5d9fb109 in your email. )', 'type': 'server_error',
'param' : None, 'code' : None} }

<!-- PageBreak -->

<!-- PageHeader="〔〕 テーブルを展開する" -->


<table>
<tr>
<th>モデル ID</th>
<th>Description</th>
<th>コンテキスト ウィンドウ</th>
<th>最大出力トーク ン</th>
<th>トレーニング データ(最 大)</th>
</tr>
<tr>
<td>gpt-4.1 (2025-04-14)</td>
<td>- テキストと画像の入力 - テキスト出力 - チャット完了 API - レスポンスAPI -ストリーミング - 関数呼び出し - 構造化された出力(チャット補 完)</td>
<td>- 1,047,576 - 128,000 (プロビジョニングされたマネージド デプ ロイ) - 300,000 (バッチ デプロイ)</td>
<td>32,768</td>
<td>2024 年5月31日</td>
</tr>
<tr>
<td rowspan="2">gpt-4.1-nano (2025-04- 14)</td>
<td>- テキストと画像の入力</td>
<td rowspan="2">- 1,047,576 - 128,000 (プロビジョニングされたマネージド デプ ロイ) - 300,000 (バッチ デプロイ)</td>
<td rowspan="2">32,768</td>
<td rowspan="2">2024 年5月31日</td>
</tr>
<tr>
<td>- テキスト出力 - チャット完了 API - レスポンスAPI -ストリーミング - 関数呼び出し - 構造化された出力(チャット補 完)</td>
</tr>
<tr>
<td>gpt-4.1-mini (2025-04- 14)</td>
<td>- テキストと画像の入力 - テキスト出力 - チャット完了 API - レスポンスAPI -ストリーミング - 関数呼び出し - 構造化された出力(チャット補 完)</td>
<td>- 1,047,576 - 128,000 (プロビジョニングされたマネージド デプ ロイ) - 300,000 (バッチ デプロイ)</td>
<td>32,768</td>
<td>2024 年5月31日</td>
</tr>
</table>


# computer-use-preview

Responses API コンピューター使用ツールで使用するためにトレーニングされた実験モデル。

サーとパーティ製ライブラリと共に使用すると、モデルは現在の環境のスクリーンショットからコンテキストを取得しながら、マウスとキーボ
ードの入力を制御できます。


## ♡ 注意事項

運用環境でプレビュー モデルを使用することはおすすめしません。プレビュー モデルのすべてのデプロイを、将来のプレビュー バージョ
ンまたは最新の安定した一般公開バージョンにアップグレードします。プレビューに指定されたモデルは、標準の Azure OpenAl モデルの
ライフサイクルに従っていません。

computer-use-preview にアクセスするには登録が必要です。アクセスは、Microsoft の資格条件に基づいて付与されます。他の制限付きアクセ
ス モデルにアクセスできるお客様は、引き続きこのモデルへのアクセスを要求する必要があります。

アクセスを要求するには、computer-use-preview 制限付きアクセス モデル アプリケーション にアクセスしてください アクセスが付与された
ら、モデルのデプロイを作成する必要があります。


# リージョンの可用性

に テーブルを展開する


<table>
<tr>
<th>モデル</th>
<th>リージョン</th>
</tr>
<tr>
<td>computer-use-preview</td>
<td>「モデル テーブル」を参照してください。</td>
</tr>
</table>


# 能力

<!-- PageFooter="〔〕 テーブルを展開する" -->
<!-- PageBreak -->


<table>
<tr>
<th>モデル ID</th>
<th>Description</th>
<th>コンテキスト ウィン ドウ</th>
<th>最大出力トー クン</th>
<th>トレーニング データ (最大)</th>
</tr>
<tr>
<td rowspan="2">computer-use-preview (2025- 03-11)</td>
<td>Responses API コンピューター使用ツールで使用するための 特殊なモデル ーツール</td>
<td rowspan="2">8,192</td>
<td rowspan="2">1,024</td>
<td>2023 年 10月</td>
</tr>
<tr>
<td>-ストリーミング - テキスト(入力と出力) - 画像(入力)</td>
<td></td>
</tr>
</table>


# ○ シリーズ モデル

Azure OpenAl o シリーズ モデルは、集中力と能力を高め、推論と問題解決のタスクに取り組むために設計されています。これらのモデルは、
ユーザーの要求の処理と理解により多くの時間を費やし、これまでの反復と比較して、科学、コーディング、数学などの分野で非常に強力にな
っています。

〔〕 テーブルを展開する


<table>
<tr>
<th>モデル ID</th>
<th>Description</th>
<th>最大要求(トー クン)</th>
<th>トレーニング デー タ(最大)</th>
</tr>
<tr>
<td>codex-mini (2025- 05-16)</td>
<td>o4-miniの微調整化バージョン。 - 応答 API。 - 構造化出力 - テキストと画像処理。 - 関数とツール。 機能の完全な要約。</td>
<td>入力:200,000 出力:100,000</td>
<td>2024 年5月31日</td>
</tr>
<tr>
<td>o3-pro (2025-06- 10)</td>
<td>- 応答 API。 - 構造化出力 - テキストと画像処理。 - 関数とツール。 機能の完全な要約。</td>
<td>入力:200,000 出力:100,000</td>
<td>2024 年5月31日</td>
</tr>
<tr>
<td>o4-mini (2025-04- 16)</td>
<td>- 新しい推論モデル。強化された推論能力を提供します。 - Chat Completions API. - 応答 API。 - 構造化出力 - テキストと画像処理。 - 関数とツール。 機能の完全な要約。</td>
<td>入力:200,000 出力:100,000</td>
<td>2024 年 5月31日</td>
</tr>
<tr>
<td>o3 (2025-04-16)</td>
<td>- 新しい推論モデル。強化された推論能力を提供します。 - Chat Completions API. - 応答 API。 - 構造化出力 - テキストと画像処理。 - 関数、ツール、および並列ツール呼び出し。 機能の完全な要約。</td>
<td>入力:200,000 出力:100,000</td>
<td>2024 年5月31日</td>
</tr>
<tr>
<td>o3-mini (2025-01- 31)</td>
<td>- 推論能力の強化。 - 構造化出力 - テキストのみの処理 - 関数とツール。</td>
<td>入力:200,000 出力:100,000</td>
<td>2023 年 10月</td>
</tr>
<tr>
<td>o1 (2024-12-17)</td>
<td>- 推論能力の強化。 - 構造化出力 - テキストと画像処理。 - 関数とツール。</td>
<td>入力:200,000 出力:100,000</td>
<td>2023 年 10月</td>
</tr>
<tr>
<td>o1-preview (2024- 09-12)</td>
<td>以前のプレビュー バージョン</td>
<td>入力:128,000 出力:32,768</td>
<td>2023 年 10月</td>
</tr>
<tr>
<td>o1-mini (2024-09- 12)</td>
<td>01シリーズのより速く、よりコスト効率の高いオプションで、速度とリソース消費の削減を必要と するタスクのコーディングに最適です。 - グローバル標準の展開が既定で使用できるようになりました。 - 現在、標準(リージョン)のデプロイは、o1-preview の制限付きアクセス リリースの一部としてア クセスが付与されたお客様のみが利用できます。</td>
<td>入力:128,000 出力:65,536</td>
<td>2023 年10月</td>
</tr>
</table>


高度な o シリーズ モデルの詳細については、「推論モデルの概要」を参照してください。

<!-- PageBreak -->

<!-- PageHeader="リージョンの可用性" -->
<!-- PageHeader="〔〕 テーブルを展開する" -->


<table>
<tr>
<td>モデル</td>
<td>リージョン</td>
</tr>
<tr>
<td>codex- mini</td>
<td>米国東部2 およびスウェーデン中部(グローバル標準)。</td>
</tr>
<tr>
<td>o3-pro</td>
<td>米国東部 2 およびスウェーデン中部(グローバル標準)。</td>
</tr>
<tr>
<td>o4-mini</td>
<td>「モデル テーブル」を参照してください。</td>
</tr>
<tr>
<td>o3</td>
<td>「モデル テーブル」を参照してください。</td>
</tr>
<tr>
<td>o3-mini</td>
<td>「モデル テーブル」を参照してください。</td>
</tr>
<tr>
<td>o1</td>
<td>「モデル テーブル」を参照してください。</td>
</tr>
<tr>
<td>o1- preview</td>
<td>「モデル テーブル」を参照してください。このモデルは、元の制限付きアクセスの一部としてアクセス権が付与されたお客様のみが使用できま す。</td>
</tr>
<tr>
<td>o1-mini</td>
<td>「モデル テーブル」を参照してください。</td>
</tr>
</table>


# GPT-4oおよびGPT-4 Turbo

GPT-4oは、テキストと画像を1つのモデルに統合し、複数のデータ型を同時に処理できるようにします。このマルチモーダルアプローチによ
り、人間とコンピューターの対話における精度と応答性が向上します。GPT-40 は、英語以外の言語のタスクやビジョン タスクで優れたパフォ
ーマンスを提供しながら、英語テキストおよびコーディング タスクの GPT-4 Turbo と一致し、AI 機能の新しいベンチマークを設定します。


# GPT-4 モデルと GPT-4 Turbo モデル

これらのモデルは、Chat Completions API でのみ使用できます。

Azure OpenAl がモデル バージョンのアップグレードを処理する方法については、「モデル バージョン」を参照してください。 GPT-4 デプロイ
のモデル バージョン設定を表示および構成する方法については、「モデルの操作」を参照してください。


<table>
<caption>〔〕 テーブルを展開する</caption>
<tr>
<th>モデル ID</th>
<th>Description</th>
<th>最大要求(トー クン)</th>
<th>トレーニング データ (最大)</th>
</tr>
<tr>
<td rowspan="2">gpt-4o (2024-11-20) GPT-4o (オムニ)</td>
<td>- 構造化出力</td>
<td>入力:128,000</td>
<td rowspan="2">2023 年 10月</td>
</tr>
<tr>
<td>- テキストと画像処理。 - JSON モード。 - 並列関数呼び出し。 - 精度と応答性の向上。 - GPT-4 Turbo with Vision と比較した英語のテキストおよびコーディング タスクを含む Parityo - 英語以外の言語とビジョン タスクでの優れたパフォーマンス。 クリエイティブ ライティング能力の向上。</td>
<td>出力:16,384</td>
</tr>
<tr>
<td>gpt-4o (2024-08-06) GPT-4o (オムニ)</td>
<td>- 構造化出力 - テキストと画像処理。 - JSON モード。 - 並列関数呼び出し。 - 精度と応答性の向上。 - GPT-4 Turbo with Vision と比較した英語のテキストおよびコーディング タスクを含む Parity. - 英語以外の言語とビジョン タスクでの優れたパフォーマンス。</td>
<td>入力:128,000 出力:16,384</td>
<td>2023 年10月</td>
</tr>
<tr>
<td rowspan="2">gpt-4o-mini (2024-07- 18) GPT-4o mini</td>
<td>- GPT-3.5 Turbo シリーズのモデルを置き換えるのに最適な、高速で安価で高機能のモデ ル。</td>
<td rowspan="2">入力:128,000 出力:16,384</td>
<td rowspan="2">2023 年 10月</td>
</tr>
<tr>
<td>- テキストと画像処理。 - JSON モード。 - 並列関数呼び出し。</td>
</tr>
<tr>
<td>gpt-4o (2024-05-13) GPT-4o (オムニ)</td>
<td>- テキストと画像処理。 - JSON モード。 - 並列関数呼び出し。</td>
<td>入力:128,000 出力:4,096</td>
<td>2023 年10月</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th>モデル ID</th>
<th>Description</th>
<th>最大要求(トー クン)</th>
<th>トレーニング データ (最大)</th>
</tr>
<tr>
<td></td>
<td>- 精度と応答性の向上。 - GPT-4 Turbo with Vision と比較した英語のテキストおよびコーディング タスクを含む Parityo - 英語以外の言語とビジョン タスクでの優れたパフォーマンス。</td>
<td></td>
<td></td>
</tr>
<tr>
<td>gpt-4 (turbo-2024-04- 09) GPT-4 ターボ ウィズビ ジョン</td>
<td>新しい一般提供モデル。 - 以前のすべての GPT-4 プレビュー モデル(vision-preview、1106-Preview、0125- Preview) についての代替モデル。 - 機能の可用性は、現在、入力方法とデプロイの種類によって異なります。</td>
<td>入力:128,000 出力:4,096</td>
<td>2023 年12月</td>
</tr>
</table>


# ♡ 注意事項

運用環境ではプレビュー モデルを使用しないことをお勧めします。プレビュー モデルのすべてのデプロイを、将来のプレビュー バージョ
ンまたは最新の安定した一般公開バージョンにアップグレードします。プレビューに指定されたモデルは、標準の Azure OpenAl モデルの
ライフサイクルに従っていません。


# GPT-3.5

GPT-3.5 モデルは、自然言語とコードを理解および生成できます。GPT-3.5 ファミリで最も優れたコスト効率の高いモデルは GPT-3.5 Turbo で
あり、チャット用に最適化されており、従来の完了タスクにも適しています。GPT-3.5 Turbo は、Chat Completions API で使用できます。GPT-
3.5 Turbo Instruct には、Chat Completions API の代わりに Completions API を使用する場合に text-davinci-003 するのと同様の機能がありま
す。GPT-3.5 および GPT-3 のレガシ モデルよりも GPT-3.5 Turbo および GPT-3.5 Turbo Instruct を使用することをお勧めします。


<table>
<caption>〔〕 テーブルを展開する</caption>
<tr>
<th>モデル ID</th>
<th>Description</th>
<th>最大要求(トー クン)</th>
<th>トレーニング データ (最大)</th>
</tr>
<tr>
<td>gpt-35-turbo (0125) new</td>
<td>- JSON モード。 - 並列関数呼び出し。 - 再現可能な出力(プレビュー)。 - 要求された形式で応答するときの精度が高くなります。 - 英語以外の関数呼び出しでテキスト エンコードの問題を引き起こしたバグの修正プログ ラムが含まれています。</td>
<td>入力:16,385 出力:4,096</td>
<td>2021 年9月</td>
</tr>
<tr>
<td>gpt-35-turbo (1106)</td>
<td>以前の一般提供モデル。 - JSON モード。 - 並列関数呼び出し。 - 再現可能な出力(プレビュー)。</td>
<td>入力:16,385 出力:4,096</td>
<td>2021 年9月</td>
</tr>
<tr>
<td>gpt-35-turbo-instruct (0914)</td>
<td>補完エンドポイントのみ。 - レガシ補完モデルの置き換え</td>
<td>4,097</td>
<td>2021 年9月</td>
</tr>
</table>


GPT-3.5 Turbo と Chat Completions API を操作する方法の詳細については、詳細なハウツー記事を参照してください。


# 埋め込み

text-embedding-3-large は、最新かつ最も高性能の埋め込みモデルです。埋め込みモデル間でアップグレードすることはできません。 text-
embedding-ada-002 を使用して text-embedding-3-large に移行するには、新しい埋め込みを生成する必要があります。

· text-embedding-3-large

. text-embedding-3-small

· text-embedding-ada-002

OpenAl レポートでは、テストでは、大規模および小規模の第3 世代埋め込みモデルの両方が MIRACL ベンチマークを使用して平均多言語取
得パフォーマンスを向上することを示しています。 MTEB ベンチマークを使用して、英語のタスクのパフォーマンスを引き続き維持します。

〔〕 テーブルを展開する


<table>
<tr>
<th>評価ベンチマーク</th>
<th>text-embedding-ada-002</th>
<th>text-embedding-3-small</th>
<th>text-embedding-3-large</th>
</tr>
<tr>
<td>MIRACL 平均</td>
<td>31.4</td>
<td>44.0</td>
<td>54.9</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th>評価ベンチマーク</th>
<th>text-embedding-ada-002</th>
<th>text-embedding-3-small</th>
<th>text-embedding-3-large</th>
</tr>
<tr>
<td>MTEB 平均</td>
<td>61.0</td>
<td>62.3</td>
<td>64.6</td>
</tr>
</table>


第3 世代の埋め込みモデルは、新しい dimensions パラメーターを使った埋め込みのサイズ削減をサポートしています。通常、埋め込みが大き
くなると、コンピューティング、メモリ、ストレージの観点からコストが高くなります。ディメンションの数を調整できる場合は、全体的なコ
ストとパフォーマンスをより詳細に制御できます。dimensionsパラメーターは、OpenAI 1.x Pythonライブラリのすべてのバージョンでサポー
トされているわけではありません。このパラメーターを利用するには、最新バージョン pip install openai -- upgrade にアップグレードするこ
とをお勧めします。

OpenAl の MTEB ベンチマーク テストでは、第3世代モデルのディメンションが text-embeddings-ada-002 の 1,536 ディメンションより小さい
場合でも、パフォーマンスは依然として若干良いことが判りました。


# 画像生成モデル

画像生成モデルは、ユーザーが提供するテキスト プロンプトから画像を生成します。GPT-image-1 シリーズ モデルは、制限付きアクセス プレ
ビュー段階です。 DALL-E 3 は、REST API との併用で一般提供されています。クライアント SDK を使用する DALL-E 2 と DALL-E 3 は、プレビュ
一段階です。

gpt-image-1 または gpt-image-1-mini にアクセスするには、登録が必要です。アクセスは、Microsoft の資格条件に基づいて付与されます。他の
制限付きアクセス モデルにアクセスできるお客様は、引き続きこのモデルへのアクセスを要求する必要があります。

アクセスを要求するには、gpt-image-1 制限付きアクセス モデル アプリケーション にアクセスしてください アクセスが付与されたら、モデ
ルのデプロイを作成する必要があります。


# リージョンの可用性

〔〕 テーブルを展開する


<table>
<tr>
<th>モデル</th>
<th>リージョン</th>
</tr>
<tr>
<td rowspan="3">dall-e-3</td>
<td>米国東部</td>
</tr>
<tr>
<td>オーストラリア東部</td>
</tr>
<tr>
<td>スウェーデン中部</td>
</tr>
<tr>
<td>gpt-image-1</td>
<td>米国西部 3(グローバル標準) 米国東部地域 2 (グローバル標準) アラブ首長国連邦北部(グローバル標準) ポーランド中部(グローバル標準) スウェーデン中部(グローバル標準)</td>
</tr>
<tr>
<td>gpt-image-1-mini</td>
<td>米国西部 3(グローバル標準) 米国東部地域 2 (グローバル標準) アラブ首長国連邦北部(グローバル標準) ポーランド中部(グローバル標準) スウェーデン中部(グローバル標準)</td>
</tr>
</table>


# ビデオ生成モデル

Soraは、テキストからの指示で現実的で想像力豊かなビデオシーンを作成できる、OpenAlによるAIモデルです。Sora はプレビュー段階です。


# リージョンの可用性

〔〕 テーブルを展開する


<table>
<tr>
<th>モデル</th>
<th>リージョン</th>
</tr>
<tr>
<td>sora</td>
<td>米国東部 2 (グローバル標準) スウェーデン中部(グローバル標準)</td>
</tr>
<tr>
<td>sora-2</td>
<td>米国東部 2 (グローバル標準) スウェーデン中部(グローバル標準)</td>
</tr>
</table>


<!-- PageBreak -->


# オーディオ モデル

Azure OpenAl のオーディオ モデルは、 realtime、completions、 audio API を介して使用できます。


## GPT-4oオーディオモデル

GPT 40 audio モデルは GPT-40 モデル ファミリの一部であり、低遅延の“音声入力、音声出力" の会話のやり取りまたはオーディオ生成のいず
れかをサポートします。


### ♡ 注意事項

運用環境でプレビュー モデルを使用することはおすすめしません。プレビュー モデルのすべてのデプロイを、将来のプレビュー バージョ
ンまたは最新の安定した一般公開バージョンにアップグレードします。プレビューに指定されたモデルは、標準の Azure OpenAl モデルの
ライフサイクルに従っていません。

次の表では、最大要求トークン数とトレーニング データに関する詳細を確認できます:


<table>
<caption>〔〕 テーブルを展開する</caption>
<tr>
<th>モデル ID</th>
<th>Description</th>
<th>最大要求(トークン)</th>
<th>トレーニング データ(最大)</th>
</tr>
<tr>
<td>gpt-4o-mini-audio-preview (2024-12-17) GPT-4oオーディオ</td>
<td>オーディオとテキスト生成向けのオーディオ モデル。</td>
<td>入力:128,000 出力:16,384</td>
<td>2023 年9月</td>
</tr>
<tr>
<td>gpt-4o-audio-preview (2024-12-17) GPT-4oオーディオ</td>
<td>オーディオとテキスト生成向けのオーディオ モデル。</td>
<td>入力:128,000 出力:16,384</td>
<td>2023 年9月</td>
</tr>
<tr>
<td>gpt-4o-realtime-preview (2025-06-03) GPT-4oオーディオ</td>
<td>リアルタイム オーディオ処理向けのオーディオ モデル。</td>
<td>入力:128,000 出力:4,096</td>
<td>2023 年10月</td>
</tr>
<tr>
<td>gpt-4o-realtime-preview (2024-12-17) GPT-4oオーディオ</td>
<td>リアルタイム オーディオ処理向けのオーディオ モデル。</td>
<td>入力:128,000 出力:4,096</td>
<td>2023 年10月</td>
</tr>
<tr>
<td>gpt-4o-mini-realtime-preview (2024-12-17) GPT-4oオーディオ</td>
<td>リアルタイム オーディオ処理向けのオーディオ モデル。</td>
<td>入力:128,000 出力:4,096</td>
<td>2023 年10月</td>
</tr>
<tr>
<td>gpt-realtime (2025年08月28日) (GA) gpt-realtime-mini (2025-10-06) gpt-audio (2025年8月28日) gpt-audio-mini (2025-10-06)</td>
<td>リアルタイム オーディオ処理向けのオーディオ モデル。</td>
<td>入力:28,672 出力:4,096</td>
<td>2023 年 10月</td>
</tr>
</table>


すべてのリージョンでの GPT-40 オーディオ モデルの可用性を比較するには、モデルの表を参照してください。


## Audio API

/audio API を介したオーディオ モデルは、音声テキスト変換、翻訳、テキスト読み上げに使用できます。


## 音声テキスト変換モデル


<table>
<caption>〔〕 テーブルを展開する</caption>
<tr>
<th>モデル ID</th>
<th>Description</th>
<th>最大要求数(オーディオ ファイル サイズ)</th>
</tr>
<tr>
<td>whisper</td>
<td>汎用音声認識モデル。</td>
<td>25 MB</td>
</tr>
<tr>
<td>gpt-4o-transcribe</td>
<td>GPT-40 を搭載した音声テキスト変換モデル。</td>
<td>25 MB</td>
</tr>
<tr>
<td>gpt-4o-mini-transcribe</td>
<td>GPT-4o mini を搭載した音声テキスト変換モデル。</td>
<td>25 MB</td>
</tr>
<tr>
<td>gpt-4o-transcribe-diarize</td>
<td>自動音声認識を使用した音声テキスト変換モデル。</td>
<td>25 MB</td>
</tr>
</table>


<!-- PageFooter="音声翻訳モデル" -->
<!-- PageFooter="〔〕 テーブルを展開する" -->
<!-- PageBreak -->


<table>
<tr>
<th>モデル ID</th>
<th>Description</th>
<th>最大要求数(オーディオ ファイル サイズ)</th>
</tr>
<tr>
<td>whisper</td>
<td>汎用音声認識モデル。</td>
<td>25 MB</td>
</tr>
</table>


## テキスト読み上げモデル(プレビュー)

〔〕 テーブルを展開する


<table>
<tr>
<th>モデル ID</th>
<th>Description</th>
</tr>
<tr>
<td>tts</td>
<td>速度に合わせて最適化されたテキスト読み上げモデル。</td>
</tr>
<tr>
<td>tts-hd</td>
<td>品質に最適化されたテキスト読み上げモデル。</td>
</tr>
<tr>
<td>gpt-4o-mini-tts</td>
<td>GPT-4o mini を搭載したテキスト読み上げモデル。</td>
</tr>
<tr>
<td></td>
<td>特定のスタイルまたはトーンで話すように音声をガイドできます。</td>
</tr>
</table>


詳細については、この記事で後述する「オーディオ モデルのリージョンの可用性」を参照してください。


# モデルの概要テーブルとリージョンの可用性


## デプロイの種類別モデル

Azure OpenAl では、お客様はビジネスと使用のパターンに合ったホスティング構造を選択できます。このサービスで提供されるデプロイの 2
つの主要な種類は、以下のとおりです。

● 標準: グローバル展開オプションがあり、トラフィックをグローバルにルーティングしてスループットを向上させます。

● プロビジョニング済み: また、グローバル デプロイ オプションを使用して、プロビジョニングされたスループット ユニットを購入して
Azure グローバル インフラストラクチャ全体にデプロイできます。

すべてのデプロイでまったく同じ推論操作を実行できますが、請求、スケール、パフォーマンスは大きく異なります。Azure OpenAl のデプロ
イの種類の詳細については、「デプロイの種類に関するガイド」を参照してください。

グローバル標準


## グローバル標準モデルの提供状況


<table>
<caption>〔〕 テーブルを展開する</caption>
<tr>
<th rowspan="2">リージョン</th>
<th>gpt-</th>
<th>gpt-5-</th>
<th>gpt-5-</th>
<th>gpt-</th>
<th>o3-</th>
<th>codex-</th>
<th>sora.</th>
<th>model-</th>
<th>model-</th>
<th>03.</th>
<th>o4-</th>
<th>gpt-</th>
<th>gpt-</th>
<th>gpt-</th>
<th>gpt-</th>
<th colspan="2">gpt-</th>
</tr>
<tr>
<td>5.</td>
<td>mini.</td>
<td>nano.</td>
<td>5-</td>
<td>pro.</td>
<td>mini.</td>
<td>2025-</td>
<td>router,</td>
<td>router,</td>
<td>2025-</td>
<td>mini.</td>
<td>image-</td>
<td>image-</td>
<td>4.1.</td>
<td>4.1-</td>
<td colspan="2">4.1-</td>
</tr>
<tr>
<td></td>
<td>2025-</td>
<td>2025-</td>
<td>2025-</td>
<td>chat,</td>
<td>2025-</td>
<td>2025-</td>
<td>05-02</td>
<td>2025-</td>
<td>2025-</td>
<td>04-16</td>
<td>2025-</td>
<td>1.</td>
<td>1-</td>
<td>2025-</td>
<td>nano.</td>
<td colspan="2">mini.</td>
</tr>
<tr>
<td></td>
<td>08-07</td>
<td>08-07</td>
<td>08-07</td>
<td>2025-</td>
<td>06-10</td>
<td>05-16</td>
<td></td>
<td>08-07</td>
<td>05-19</td>
<td></td>
<td>04-16</td>
<td>2025-</td>
<td>mini.</td>
<td>04-14</td>
<td>2025-</td>
<td colspan="2">2025-</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td>08-07</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>04-15</td>
<td>2025-</td>
<td></td>
<td>04-14</td>
<td colspan="2">04-14</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>10-06</td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr>
<td>オーストラリア イースト</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td colspan="2">-</td>
</tr>
<tr>
<td>ブラジルサウス</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>☒ ✅</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>☒ ✅</td>
<td>-</td>
<td></td>
<td>-</td>
</tr>
<tr>
<td>カナダ東部</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>☒ ✅</td>
<td>-</td>
<td colspan="2">-</td>
</tr>
<tr>
<td>イーストアス</td>
<td>☒ ✅</td>
<td>☒ ✅</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>☒ ✅</td>
<td>☒ ✅</td>
<td>-</td>
<td>☒ ✅</td>
<td>-</td>
<td>✅ ☒</td>
<td colspan="2">-</td>
</tr>
<tr>
<td>eastus2</td>
<td>☒ ✅</td>
<td>☒ ✅</td>
<td>☒ ✅</td>
<td>☒ ✅</td>
<td>☒ ✅</td>
<td>☒ ✅</td>
<td>☒ ✅</td>
<td>☒ ✅</td>
<td>☒ ✅</td>
<td>✅ ☒</td>
<td>☒ ✅</td>
<td>☒ ✅</td>
<td>☒ ✅</td>
<td>☒ ✅</td>
<td>☒ ✅</td>
<td></td>
<td>✅ ☒</td>
</tr>
<tr>
<td>francecentral</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>☒ ✅</td>
<td>☒ ✅</td>
<td>-</td>
<td>-</td>
<td>☒ ✅</td>
<td>-</td>
<td colspan="2">-</td>
</tr>
<tr>
<td>ドイツ中西部</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>☒ ✅</td>
<td>☒ ✅</td>
<td>-</td>
<td>-</td>
<td>☒ ✅</td>
<td>-</td>
<td></td>
<td>-</td>
</tr>
<tr>
<td>italynorth</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>☒ ✅</td>
<td>☒ ✅</td>
<td>-</td>
<td>-</td>
<td>☒ ✅</td>
<td>-</td>
<td></td>
<td>-</td>
</tr>
<tr>
<td>japaneast</td>
<td>☒ ✅</td>
<td>☒ ✅</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>☒ ✅</td>
<td>☒ ✅</td>
<td>-</td>
<td>-</td>
<td>☒ ✅</td>
<td>-</td>
<td></td>
<td>-</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th rowspan="2">リージョン</th>
<th>gpt-</th>
<th>gpt-5-</th>
<th>gpt-5-</th>
<th>gpt-</th>
<th>o3-</th>
<th>codex-</th>
<th>sora.</th>
<th>model-</th>
<th>model-</th>
<th>03.</th>
<th>o4-</th>
<th>gpt-</th>
<th>gpt-</th>
<th>gpt-</th>
<th>gpt-</th>
<th>gpt-</th>
</tr>
<tr>
<th>5.</th>
<th>mini.</th>
<th>nano.</th>
<th>5-</th>
<th>pro.</th>
<th>mini.</th>
<th>2025-</th>
<th>router,</th>
<th>router,</th>
<th>2025-</th>
<th>mini.</th>
<th>image-</th>
<th>image-</th>
<th>4.1.</th>
<th>4.1-</th>
<th>4.1-</th>
</tr>
<tr>
<td></td>
<td>2025-</td>
<td>2025-</td>
<td>2025-</td>
<td>chat,</td>
<td>2025-</td>
<td>2025-</td>
<td>05-02</td>
<td>2025-</td>
<td>2025-</td>
<td>04-16</td>
<td>2025-</td>
<td>1.</td>
<td>1-</td>
<td>2025-</td>
<td>nano.</td>
<td>mini.</td>
</tr>
<tr>
<td></td>
<td>08-07</td>
<td>08-07</td>
<td>08-07</td>
<td>2025-</td>
<td>06-10</td>
<td>05-16</td>
<td></td>
<td>08-07</td>
<td>05-19</td>
<td></td>
<td>04-16</td>
<td>2025-</td>
<td>mini.</td>
<td>04-14</td>
<td>2025-</td>
<td>2025-</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td>08-07</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>04-15</td>
<td>2025-</td>
<td></td>
<td>04-14</td>
<td>04-14</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>10-06</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>コリアセントラ ル</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>ノースセントラ JLUS</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>ノルウェーイー スト</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>polandcentral</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>southafricanorth</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>サウスセントラ ル</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>南インド</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>spaincentral</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>swedencentral</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>スイスノース</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>uaenorth</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>ウクサウス</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>西ヨーロッパ</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>ウェストユーエ ス</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>☒ ✅</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>westus3</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td rowspan="2">-</td>
<td rowspan="2">✅ ☒</td>
<td rowspan="2">✅ ☒</td>
<td>✅ ☒</td>
<td rowspan="2">-</td>
<td rowspan="2">✅ ☒</td>
<td rowspan="2">-</td>
<td rowspan="2">-</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>


1 Note
☒

03-deep-research は現在、Foundry Agent Service でのみ使用できます。詳細については、ディープ リサーチ ツールのガイダンスを参
照してください。

この表には、リージョンごとの提供状況の微調整に関する情報は含まれていません。この情報については、微調整のセクション を参照してく
ださい。


## エンドポイント別の標準デプロイ(リージョン)モデル

チャットの完了


## チャットの完了

〔〕 テーブルを展開する


<table>
<tr>
<th>リージョン</th>
<th>o1-preview. 2024-09-12</th>
<th>o1-mini. 2024-09-12</th>
<th>gpt-40. 2024 年5月 13 日</th>
<th>gpt-40. 2024-11-20</th>
<th>gpt-40. 2024-08- 06</th>
<th>gpt-4o- mini. 2024- 07-18</th>
<th>gpt-4. turbo-2024- 04-09</th>
<th>gpt-35- turbo. 1106</th>
<th>gpt-35- turbo. 0125</th>
</tr>
<tr>
<td>オーストラリアイ ースト</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>☒ ✅</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>☒ ✅</td>
<td>☒ ✅</td>
</tr>
<tr>
<td>カナダ東部</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>☒ ✅</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>☒ ✅</td>
<td>☒ ✅</td>
</tr>
<tr>
<td>イーストアス</td>
<td>☒ ✅</td>
<td>☒ ✅</td>
<td>☒ ✅</td>
<td>☒ ✅</td>
<td>☒ ✅</td>
<td>☒ ✅</td>
<td>☒ ✅</td>
<td>-</td>
<td>☒ ✅</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th>リージョン</th>
<th>01-preview. 2024-09-12</th>
<th>o1-mini. 2024-09-12</th>
<th>gpt-40. 2024年5月 13 日</th>
<th>gpt-40. 2024-11-20</th>
<th>gpt-40. 2024-08- 06</th>
<th>gpt-4o- mini. 2024- 07-18</th>
<th>gpt-4. turbo-2024- 04-09</th>
<th>gpt-35- turbo. 1106</th>
<th>gpt-35- turbo. 0125</th>
</tr>
<tr>
<td>eastus2</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>✅ ☒</td>
</tr>
<tr>
<td>francecentral</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
</tr>
<tr>
<td>japaneast</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
</tr>
<tr>
<td>ノースセントラル US</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>✅ ☒</td>
</tr>
<tr>
<td>ノルウェーイース ト</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>サウスセントラ ル</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>✅ ☒</td>
</tr>
<tr>
<td>南インド</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
</tr>
<tr>
<td>swedencentral</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
</tr>
<tr>
<td>スイスノース</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
</tr>
<tr>
<td>ウクサウス</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
</tr>
<tr>
<td>西ヨーロッパ</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
</tr>
<tr>
<td>ウェストユーエ ス</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
</tr>
<tr>
<td>westus3</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>✅ ☒</td>
</tr>
</table>


## Note

現在、o1-mini は、グローバル標準の展開のすべてのお客様が利用できます。

一部のお客様には、o1-mini 制限付きアクセス リリースの一部として、o1-preview への標準(リージョン) デプロイ アクセスが付与さ
れています。現時点では、o1-mini標準(リージョン)デプロイへのアクセスは拡張されていません。

Azure OpenAl がモデル バージョンのアップグレードを処理する方法については、「モデル バージョン」を参照してください。GPT-3.5
Turbo デプロイのモデル バージョン設定を表示および構成する方法については、「モデルを使用した作業」を参照してください。


# モデルの微調整


## 1 Note

gpt-35-turbo: このモデルの微調整はリージョンのサブセットに限定され、基本モデルが使用可能なすべてのリージョンで使用できるわけ
ではありません。

微調整でサポートされるリージョンは、Microsoft Foundry プロジェクトで Azure OpenAl モデルを使用する場合とプロジェクト外で使用す
る場合は異なる場合があります。

〔〕 テーブルを展開する


<table>
<tr>
<th>モデル ID</th>
<th>標準のトレーニングリ ージョン</th>
<th>グローバル トレー ニング</th>
<th>最大要求(トークン)</th>
<th>トレーニング データ (最大)</th>
<th>Modality</th>
</tr>
<tr>
<td>gpt-35-turbo</td>
<td>米国東部 2</td>
<td>-</td>
<td>入力:16,385</td>
<td>2021 年9月</td>
<td>テキスト間</td>
</tr>
<tr>
<td rowspan="3">(1106)</td>
<td>米国中北部</td>
<td></td>
<td>出力:4,096</td>
<td></td>
<td></td>
</tr>
<tr>
<td>スウェーデン中部</td>
<td rowspan="2"></td>
<td rowspan="2"></td>
<td rowspan="2"></td>
<td rowspan="2"></td>
</tr>
<tr>
<td>スイス西部</td>
</tr>
<tr>
<td rowspan="3">gpt-35-turbo (0125)</td>
<td>米国東部 2</td>
<td rowspan="2">-</td>
<td rowspan="2">16,385</td>
<td rowspan="3">2021 年9月</td>
<td rowspan="2">テキスト間</td>
</tr>
<tr>
<td>米国中北部</td>
</tr>
<tr>
<td>スウェーデン中部 スイス西部</td>
<td></td>
<td></td>
<td></td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th>モデル ID</th>
<th>標準のトレーニング リ ージョン</th>
<th>グローバル トレー ニング</th>
<th>最大要求(トークン)</th>
<th>トレーニング データ (最大)</th>
<th>Modality</th>
</tr>
<tr>
<td>gpt-4o-mini (2024-07-18)</td>
<td>米国中北部 スウェーデン中部</td>
<td>✅ ☒</td>
<td>入力:128,000 出力:16,384 トレーニング用コンテキストの例の長 さ:65,536</td>
<td>2023 年 10月</td>
<td>テキスト間</td>
</tr>
<tr>
<td>gpt-4o (2024-08-06)</td>
<td>米国東部 2 米国中北部 スウェーデン中部</td>
<td>✅ ☒</td>
<td>入力:128,000 出力:16,384 トレーニング用コンテキストの例の長 さ:65,536</td>
<td>2023 年 10月</td>
<td>テキストと視覚テキ スト</td>
</tr>
<tr>
<td>gpt-4.1 (2025-04-14)</td>
<td>米国中北部 スウェーデン中部</td>
<td>✅ ☒</td>
<td>入力:128,000 出力:16,384 トレーニング用コンテキストの例の長 さ:65,536</td>
<td>2024 年5月</td>
<td>テキストと視覚テキ スト</td>
</tr>
<tr>
<td rowspan="2">gpt-4.1-mini (2025-04-14)</td>
<td>米国中北部 スウェーデン中部</td>
<td rowspan="2">✅ ☒</td>
<td rowspan="2">入力:128,000 出力:16,384 トレーニング用コンテキストの例の長 さ:65,536</td>
<td rowspan="2">2024 年5月</td>
<td rowspan="2">テキスト間</td>
</tr>
<tr>
<td></td>
</tr>
<tr>
<td>gpt-4.1-nano (2025- 04-14)</td>
<td>米国中北部 スウェーデン中部</td>
<td>✅ ☒</td>
<td>入力:128,000 出力:16,384 トレーニング例のコンテキスト長: 32,768</td>
<td>2024 年5月</td>
<td>テキスト間</td>
</tr>
<tr>
<td>o4-mini (2025-04-16)</td>
<td>米国東部 2 スウェーデン中部</td>
<td>-</td>
<td>入力:128,000 出力:16,384 トレーニング用コンテキストの例の長 さ:65,536</td>
<td>2024 年5月</td>
<td>テキスト間</td>
</tr>
</table>


## 1 Note

グローバル トレーニングでは、トークンごとに より手頃な価格 のトレーニングが提供されますが、データ所在地 は提供されません。
現在、次のリージョンの Azure OpenAl リソースで使用できます。

● オーストラリア東部

· ブラジル南部

● カナダ中部

● カナダ東部

● 米国東部

● 米国東部 2

· フランス中部

· ドイツ中西部

● イタリア北部

● 東日本(ビジョンサポートなし)

● 韓国中部

● 米国中北部

● ノルウェー東部

● ポーランド中部 (4.1 ナノサポートなし)

● 東南アジア

● 南アフリカ北部

● 米国中南部

● インド南部

● スペイン中部

● スウェーデン中部

● スイス西部

● スイス北部

● 英国南部

· 西ヨーロッパ

● 米国西部

<!-- PageBreak -->

<!-- PageHeader="● 米国西部 3" -->


# アシスタント(プレビュー)

アシスタントについては、サポートされているモデルとサポートされているリージョンの組み合わせが必要です。特定のツールと機能には最新
モデルが必要です。 Assistants API、SDK、Foundry では、次のモデルを使用できます。次の表は、標準のデプロイ用です。プロビジョニング
されたスループット ユニットの可用性の詳細については、「プロビジョニングされたスループット」を参照してください。一覧で示されている
モデルとリージョンは、Assistants v1 と v2 の両方で使用できます。グローバル標準モデルは、次のリージョンでサポートされている場合に使
用できます。

〔〕 テーブルを展開する


<table>
<tr>
<th rowspan="2">リージョン</th>
<th rowspan="2">gpt- 4o,2024- 05-13</th>
<th rowspan="2">gpt-4o, 2024- 08-06</th>
<th rowspan="2">gpt-4o- mini, 2024-07- 18</th>
<th rowspan="2">gpt- 4, 0613</th>
<th rowspan="2">gpt-4. 1106- Preview</th>
<th rowspan="2">gpt-4. 0125- Preview</th>
<th rowspan="2">gpt-4. turbo- 2024- 04-09</th>
<th rowspan="2">gpt-4- 32k, 0613</th>
<th rowspan="2">gpt-35- turbo. 0613</th>
<th rowspan="2">gpt-35- turbo, 1106</th>
<th rowspan="2">gpt-35- turbo,0125</th>
<th>gpt-35- turbo- 16k,</th>
</tr>
<tr>
<td>0613</td>
</tr>
<tr>
<td>オーストラリ アイースト</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
</tr>
<tr>
<td>イーストアス</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
</tr>
<tr>
<td>eastus2</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
</tr>
<tr>
<td>francecentral</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>✅ ☒</td>
</tr>
<tr>
<td>japaneast</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
</tr>
<tr>
<td>ノルウェーイ ースト</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>南インド</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
</tr>
<tr>
<td>swedencentral</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>✅ ☒</td>
</tr>
<tr>
<td>ウクサウス</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
</tr>
<tr>
<td>ウェストユー エス</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>☒ ✅</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
</tr>
<tr>
<td>westus3</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>✅ ☒</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✅ ☒</td>
<td>-</td>
</tr>
</table>


# モデルの廃止

モデルの廃止に関する最新情報については、モデル廃止ガイドに関する記事をご覧ください。


# 関連コンテンツ

● フォンドリーのモデル:パートナーおよびコミュニティから

● モデルの廃止と非推奨

● Azure OpenAl モデルの操作に関する詳細を確認する

● Azure OpenAl の詳細についてご覧ください

● Azure OpenAl モデルの微調整に関する詳細を確認する

1 注: 作成者は AI の支援の下、この記事を作成しました。詳細情報

<!-- PageFooter="Last updated on 2025/11/13" -->
