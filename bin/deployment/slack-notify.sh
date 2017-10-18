#!/usr/bin/env bash

set -e

# usage: slack-notify <ec-instance-name>

# check for instance mapping
INSTANCE="$1"

SHA_SHORT="${CIRCLE_SHA1:0:7}"

AUTHOR_NAME="$(git show -s --format='%an' $SHA_SHORT)"
EC_INSTANCE_URL="https://templates.pinaxproject.com/"

# prepare Slack message payload
MESSAGE="${AUTHOR_NAME} deployed \`<https://github.com/pinax/pinax_theme_tester/commit/${SHA_SHORT}|${SHA_SHORT}>\` to <${EC_INSTANCE_URL}|${INSTANCE}>."
PAYLOAD_DATA="payload={\"channel\": \"#pinax-theme-tester\", \"username\": \"Deployments\", \"text\": \"${MESSAGE}\", \"icon_emoji\": \":package:\"}"

# post to Slack
echo "Sending Slack notification..."
echo $PAYLOAD_DATA
curl -XPOST "$EC_DEPLOY_WEBHOOK_URL" --data-urlencode "$PAYLOAD_DATA"

