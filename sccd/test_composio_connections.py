#!/usr/bin/env python3
"""
Direct Composio REST API Connected Accounts Checker (Stdlib Only)
Queries https://backend.composio.dev/api/v1/connectedAccounts with COMPOSIO_API_KEY
"""

import os
import json
import urllib.request

def check_connections():
    api_key = os.getenv("COMPOSIO_API_KEY", "ak_wxKeosFsuiZaLinpU7zG")
    url = "https://backend.composio.dev/api/v2/connectedAccounts"
    
    req = urllib.request.Request(
        url,
        headers={
            "x-api-key": api_key,
            "User-Agent": "Antigravity/1.0"
        }
    )
    
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            print("[SUCCESS] Composio API Connected Accounts Payload:")
            print(json.dumps(data, indent=2))
            return data
    except Exception as e:
        print(f"[ERROR] Failed to fetch connected accounts: {e}")
        return None

if __name__ == "__main__":
    check_connections()
