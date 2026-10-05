# Kalshi Settlement Calendar & Order Book Depth

Kalshi markets ranked by when they settle, with the order book depth, spread and settlement source of each one.

[![Run on Apify](https://img.shields.io/badge/Run%20on-Apify-0f9f74)](https://apify.com/datagrit/kalshi-settlement-calendar) [![Docs](https://img.shields.io/badge/docs-getdatagrit.github.io-0e1726)](https://getdatagrit.github.io/kalshi-settlement-calendar/)

**from $1.75 per 1,000 results + $10 per run (pay per result; the rate depends on your Apify plan).** Export as JSON, CSV or Excel, call it through the API, or schedule it on Apify.

## What it does

It lists the open Kalshi prediction markets that are expected to settle inside a time window you choose, for example the next 24 hours, and returns one flat row per market: expected settlement time, hours to settle, the sources Kalshi settles on, YES bid, ask and spread, 24-hour volume, open interest and the contracts resting near the best bid and ask. It is built for traders, quants and bot builders who want a settlement calendar with liquidity attached, not a dump of every market. Export the rows as JSON, CSV or Excel, call the Actor through the Apify API, or plug it into n8n, Make and AI agents through MCP.

## Quick start

1. Open [Kalshi Settlement Calendar & Order Book Depth on Apify Store](https://apify.com/datagrit/kalshi-settlement-calendar) and click **Try for free**.
2. Fill in the input form (or paste the JSON below) and run it.
3. Download the dataset, or fetch it from the API.

```json
{
  "settlesWithinHours": 48,
  "maxItems": 50
}
```

## Input

| Field | Type | What it does |
|---|---|---|
| `settlesWithinHours` | number | Keep markets whose expected settlement time is at most this many hours from now. 24 means everything that settles today and tonight; 168 is one week. |
| `settlesAfterHours` | number | Keep markets whose expected settlement time is at least this many hours from now. 0 starts at the present moment; a negative value also returns markets whose expected time has passed but which are not settled yet (for example -6). |
| `categories` | array | Optional. Only markets of series that Kalshi lists under these categories (a series can be listed under several, so a row can show another category than the one you asked for; see the categories field), for example Sports, Crypto, Financials, Politics, Economics, Transportation, Climate and Weather, Entertainment. Case-insensitive; leave empty for all categories. |
| `seriesTickers` | array | Optional. Only these Kalshi series, for example KXBTCD or KXNASDAQ100U. Scanning named series is much faster than scanning the whole exchange. |
| `keywords` | array | Optional. Keep markets whose market title contains at least one of these words or phrases (case-insensitive). Only the market title is searched, not the outcome or series name. |
| `minVolume24h` | integer | Keep markets with at least this many contracts traded in the last 24 hours. 0 turns the filter off. |
| `minOpenInterest` | integer | Keep markets with at least this many contracts outstanding. 0 turns the filter off. |
| `requireTwoSidedQuote` | boolean | Keep only markets with a YES bid of at least 1 cent and a YES ask of at most 99 cents, so that you can actually trade both ways. Turn off to also list markets that nobody quotes. |
| `maxSpreadCents` | number | Keep markets whose YES ask minus YES bid is at most this many cents. 100 turns the filter off; any lower value also drops markets that are not quoted on both sides. |
| `sortBy` | string | Order of the results before "Maximum results" is applied: soonest settlement, highest 24h volume, highest open interest or tightest spread. |
| `includeOrderbook` | boolean | Read the order book of every returned market and add the depth fields (contracts near the best bid and ask, levels, totals). Turn off for a faster run without depth. |
| `depthCents` | integer | Width of the window used by the depth fields: contracts resting within this many cents of the best bid, and within this many cents of the best ask. |
| `includeRules` | boolean | Add the primary and secondary settlement rules text of every market. Makes the rows larger. |
| `maxItems` | integer | Stop after this many markets. |
| `proxyConfiguration` | object | Optional proxy. Leave disabled: the Kalshi public API does not need one. |

## Output

| Field | Type | Description |
|---|---|---|
| `found` | boolean | False only for the single status row emitted when no market matches the input. |
| `ticker` | string | Unique Kalshi market ticker. Empty only on the status row. |
| `eventTicker` | string | Ticker of the Kalshi event the market belongs to. |
| `seriesTicker` | string | Ticker of the recurring series the event belongs to, matched to the Kalshi series catalog by the longest event ticker prefix. Null when the event matches no series in the catalog. |
| `seriesTitle` | string | Human-readable title of the series. |
| `category` | string | Primary Kalshi category of the series, for example Sports, Crypto, Financials, Politics or Climate and Weather. A series can be listed under more than one category; all of them are in categories, and the categories filter matches any of them. |
| `categories` | array | Every Kalshi category the series is listed under, the same membership the categories input filter uses. Null on the status row. |
| `frequency` | string | How often the series repeats, as published by Kalshi (hourly, daily, weekly, custom and others). |
| `title` | string | Question or statement the market settles on. |
| `outcome` | string | What a YES contract pays on, as written by Kalshi (for example the team or the price bracket). |
| `status` | string | Market status reported by Kalshi. The Actor lists markets whose status is active (open for trading) only. |
| `expectedSettlementTime` | string | ISO 8601 time at which Kalshi expects the market to settle (expected_expiration_time). This is the sort and filter key of the Actor. |
| `hoursToSettle` | number | Hours between the start of the run and the expected settlement time, rounded to 2 decimals. Negative means the expected time has passed and the market has not settled yet. |
| `closeTime` | string | ISO 8601 time after which the market stops trading at the latest. Markets that can close early often settle long before it. |
| `latestSettlementTime` | string | ISO 8601 latest time by which Kalshi will settle the market (latest_expiration_time). |
| `settlementTimerSeconds` | number | Seconds Kalshi waits after the outcome is known before it pays out the market. |
| `canCloseEarly` | boolean | True when the market closes as soon as its outcome is decided instead of waiting for the close time. |
| `settlementSources` | string | Names of the sources Kalshi uses to settle the series, joined with semicolons. Null when the series lists none. |
| `settlementSourceUrls` | string | Links to the settlement sources, separated by single spaces, in the same order as the names. |
| `yesBid` | number | Best price in dollars someone is willing to pay for a YES contract. 0 means there is no bid. |
| `yesAsk` | number | Best price in dollars at which a YES contract can be bought. 1 means there is no offer. |
| `noBid` | number | Best price in dollars someone is willing to pay for a NO contract. |
| `noAsk` | number | Best price in dollars at which a NO contract can be bought. |
| `lastPrice` | number | Price of the last trade in dollars. 0 when the market has not traded. |
| `midPrice` | number | Midpoint of the YES bid and ask in dollars, read as the implied probability of YES. Null unless the market has a bid of at least 1 cent and an ask of at most 99 cents. |
| `spreadCents` | number | YES ask minus YES bid in cents. Null unless the market is quoted on both sides. |
| `yesBidSize` | number | Contracts resting at the best YES bid. |
| `yesAskSize` | number | Contracts resting at the best YES ask. |
| `volume` | number | Contracts traded over the lifetime of the market. |
| `volume24h` | number | Contracts traded in the last 24 hours. |
| `openInterest` | number | Contracts currently held across all traders. |
| `yesBidDepth` | number | Contracts resting on the YES bid side within the depth window below the best bid. Null when the order book was skipped or unavailable. |
| `yesAskDepth` | number | Contracts available to buy YES within the depth window above the best ask (resting NO bids, which are YES offers). Null when the order book was skipped or unavailable. |
| `yesBidLevels` | number | Number of price levels on the YES bid side of the whole book. Null when the order book was skipped or unavailable. |
| `yesAskLevels` | number | Number of price levels on the YES ask side of the whole book. Null when the order book was skipped or unavailable. |
| `yesBidTotal` | number | Contracts on the YES bid side across all price levels. Null when the order book was skipped or unavailable. |
| `yesAskTotal` | number | Contracts on the YES ask side across all price levels. Null when the order book was skipped or unavailable. |
| `depthWindowCents` | number | Width in cents of the window used for the two depth fields. Null when the order book was skipped or unavailable. |
| `rulesPrimary` | string | Primary settlement rules text of the market. Present only when "Include rules text" is on. |
| `rulesSecondary` | string | Secondary settlement rules text of the market. Present only when "Include rules text" is on. |
| `sourceUrl` | string | Kalshi API URL of the market. Empty only on the status row. |
| `scrapedAt` | string | ISO 8601 time of the run. |

Sample record:

```json
{
  "found": true,
  "ticker": "KXBTCD-26OCT0117-T83249.99",
  "eventTicker": "KXBTCD-26OCT0117",
  "seriesTicker": "KXBTCD",
  "seriesTitle": "Bitcoin price Above/below",
  "category": "Crypto",
  "categories": [
    "Economics",
    "Transportation"
  ],
  "frequency": "hourly",
  "title": "Bitcoin price on Oct 1, 2026?",
  "outcome": "Dallas",
  "status": "active",
  "expectedSettlementTime": "2026-10-01T10:00:00.000Z",
  "hoursToSettle": 18.34,
  "closeTime": "2026-10-03T01:00:00.000Z",
  "latestSettlementTime": "2026-10-03T01:00:00.000Z",
  "settlementTimerSeconds": 90,
  "canCloseEarly": true,
  "settlementSources": "CF Benchmarks",
  "settlementSourceUrls": "https://www.cfbenchmarks.com/data/indices/BRTI",
  "yesBid": 0.58,
  "yesAsk": 0.59,
  "noBid": 0.41,
  "noAsk": 0.42,
  "lastPrice": 0.58,
  "midPrice": 0.585,
  "spreadCents": 1,
  "yesBidSize": 7442.21,
  "yesAskSize": 525.33,
  "volume": 29185.23,
  "volume24h": 29185.23,
  "openInterest": 17101.47,
  "yesBidDepth": 16839.01,
  "yesAskDepth": 19022.45,
  "yesBidLevels": 31,
  "yesAskLevels": 59,
  "yesBidTotal": 101444.2,
  "yesAskTotal": 150167.1,
  "depthWindowCents": 5,
  "rulesPrimary": "If Bitcoin is above 83249.99 at 5pm EDT, the market resolves to Yes.",
  "rulesSecondary": "If the source is unavailable, the market settles on the next published value.",
  "sourceUrl": "https://api.elections.kalshi.com/trade-api/v2/markets/KXBTCD-26OCT0117-T83249.99",
  "scrapedAt": "2026-10-01T02:44:42.436Z"
}
```

## Call it from code

Runnable examples are in [`examples/`](examples). Replace `YOUR_APIFY_TOKEN` with the token from your Apify account settings.

```bash
curl -X POST "https://api.apify.com/v2/acts/datagrit~kalshi-settlement-calendar/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"settlesWithinHours":48,"maxItems":50}'
```


## More from datagrit

- [Football Contract Expiry Radar - Transfermarkt](https://github.com/getdatagrit/football-contract-expiry-radar) - Football players whose contracts end soon, per league and expiry window, with market value, trend, agent and extension options from Transfermarkt end-of-contract lists.
- [Polymarket Liquidity Rewards & Book Depth](https://github.com/getdatagrit/polymarket-reward-yield-screener) - Polymarket markets that pay liquidity rewards, joined with the live order book: reward pool, qualifying depth and estimated payout per market.
- [TED Contract Expiry Radar - Recompete Leads](https://github.com/getdatagrit/ted-contract-expiry-radar) - Find EU public contracts approaching expiry from TED award notices: incumbent, buyer, value, end date and renewal options.
- [UK Contract Expiry Radar - Recompete Leads](https://github.com/getdatagrit/uk-contract-expiry-radar) - UK public contracts ending soon with incumbent supplier, buyer, value and contact - recompete leads from Contracts Finder award notices.
- [French Company Finder - Sirene Financials](https://github.com/getdatagrit/french-company-finder) - French company lead lists from Sirene screened by net result and revenue, with net margin, size, matching establishment and optional directors.

All Actors: [https://getdatagrit.github.io/](https://getdatagrit.github.io/) · [Apify Store](https://apify.com/datagrit)

---

This repository holds documentation and usage examples. Questions, bug reports and feature requests: use the **Issues** tab of the Actor page on [Apify Store](https://apify.com/datagrit/kalshi-settlement-calendar). Examples are MIT licensed.
