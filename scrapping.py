from apify_client import ApifyClient
import json
client = ApifyClient("apify_api_Z0AqmlBnlGcxbYwHTQ0wgXu4lLatRh12B97T") # Initialize the ApifyClient with your API token
run_input = {                                              # Prepare the Actor input
    "startUrls": [{ "url": "https://crawlee.dev" }],
    "keepUrlFragments": False,
    "globs": [{ "glob": "https://crawlee.dev/*/*" }],
    "pseudoUrls": [],
    "excludes": [{ "glob": "/**/*.{png,jpg,jpeg,pdf}" }],
    "linkSelector": "a[href]",
    "runScripts": True,
    "showInternalConsole": False,
    "pageFunction": """async function pageFunction(context) {
        const { window, request, log } = context;
        const pageTitle = window.document.title;
        const url = request.url;
        log.info('Page scraped', { url, pageTitle });
        return { url, pageTitle };
    }""",
    "proxyConfiguration": { "useApifyProxy": True },
    "proxyRotation": "RECOMMENDED",
    "maxRequestRetries": 3,
    "maxPagesPerCrawl": 0,
    "maxResultsPerCrawl": 0,
    "maxCrawlingDepth": 0,
    "maxConcurrency": 50,
    "pageLoadTimeoutSecs": 60,
    "pageFunctionTimeoutSecs": 60,
    "debugLog": False,
    "customData": {},     }
run = client.actor("hMvNSpz3JnHgl5jkh").call(run_input=run_input)   # Run the Actor and wait for it to finish
data = []                                             # Fetch and save Actor results to JSON file
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    data.append(item)
with open("indeed_data_program.json", "w") as json_file:     # Save data to JSON file
    json.dump(data, json_file, indent=4)
print("Results saved in indeed_data_program.json")