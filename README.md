# VirusTotal API Checker 🔍

This Python script allows you to query the [VirusTotal API](https://www.virustotal.com/) to analyze file hashes, IP addresses, and domain names for potential security threats.

## 🚀 Features

- Query file hashes (SHA256/SHA1)
- Query IP addresses
- Query domain names
- Saves the full API response to `data.json`
- Displays a summary of the scan results in the terminal

## 📦 Requirements

- Python 3.x
- Internet connection
- VirusTotal API key

## 🔧 Installation


1. Clone this repository or [download the ZIP](https://github.com/Elieveee/virustotal-api-checker/archive/refs/heads/main.zip):

```bash
git clone https://github.com/Elieveee/virustotal-api-checker.git
cd virustotal-api-checker
```

2. Run the script:

```bash
python main.py
```

## 🔑 VirusTotal API Key

To use the API, register for a free account at [VirusTotal](https://www.virustotal.com/gui/join-us) and get your personal API key.

## 📝 Usage

1. When you run the script, it will prompt you for:
   - Your API key
   - A file hash, IP address, or domain to check
2. The results will be saved to `data.json` and a summary will be printed in the console.

## 📁 Sample Output

```json
{
    "harmless": 77,
    "malicious": 0,
    "suspicious": 0,
    "undetected": 3,
    "timeout": 0
}
```

## ⚠️ Notes

- The free VirusTotal API has a rate limit (4 requests per minute).
- Keep your API key private.
- Be cautious about the contents of `data.json` when sharing results.

## 📃 License

Licensed under the MIT License.


