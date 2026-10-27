
# Test Samples and Results

## Test 1: HTTP URL

Input: `http://example.com`

Expected: Warning about HTTP instead of HTTPS.

Actual: Passed — HTTP warning displayed.

## Test 2: HTTPS URL

Input: `https://example.com`

Expected: No warning signs detected by the current checks.

Actual: Passed — no warning signs displayed.

## Test 3: URL containing @

Input: `http://example.com@evil.test`

Expected: Warnings for the @ symbol and HTTP.

Actual: Passed — both warnings displayed.

## Test 4: Long URL

Input: A URL longer than 100 characters.

Expected: Warnings for URL length and HTTP.

Actual: Passed — both warnings displayed.

## Limitations

This tool checks URL text only. It does not visit websites or prove that a URL is safe.
