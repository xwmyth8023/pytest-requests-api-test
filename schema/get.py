schema = {
  "type": "object",
  "properties": {
    "args": {
      "type": "object"
    },
    "headers": {
      "type": "object",
      "properties": {
        "Accept": {
          "type": "string"
        },
        "Accept-Encoding": {
          "type": "string"
        },
        "Accept-Language": {
          "type": "string"
        },
        "Host": {
          "type": "string"
        },
        "Sec-Ch-Ua": {
          "type": "string"
        },
        "Sec-Ch-Ua-Mobile": {
          "type": "string"
        },
        "Sec-Ch-Ua-Platform": {
          "type": "string"
        },
        "Sec-Fetch-Dest": {
          "type": "string"
        },
        "Sec-Fetch-Mode": {
          "type": "string"
        },
        "Sec-Fetch-Site": {
          "type": "string"
        },
        "Sec-Fetch-User": {
          "type": "string"
        },
        "Upgrade-Insecure-Requests": {
          "type": "string"
        },
        "User-Agent": {
          "type": "string"
        },
        "X-Amzn-Trace-Id": {
          "type": "string"
        }
      },
      "required": [
        "Accept",
        "Accept-Encoding",
        "Host",
        "User-Agent",
        "X-Amzn-Trace-Id"
      ]
    },
    "origin": {
      "type": "string"
    },
    "url": {
      "type": "string"
    }
  },
  "required": [
    "args",
    "headers",
    "origin",
    "url"
  ]
}
