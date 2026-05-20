#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
REPO_ROOT="$(cd "$ROOT/.." && pwd)"
FONT="/System/Library/Fonts/Supplemental/Arial.ttf"
MONO_FONT="/System/Library/Fonts/Menlo.ttc"
EDGE_TTS_PYTHON="${EDGE_TTS_PYTHON:-python3.11}"
EDGE_TTS_VOICE="${EDGE_TTS_VOICE:-en-US-AvaNeural}"
EDGE_TTS_RATE="${EDGE_TTS_RATE:--7%}"
OUT="$ROOT/media/human-ai-handoff-copilot-demo.mp4"
LEGACY_OUT="$ROOT/media/human-ai-handoff-copilot-demo-draft.mp4"
TMP_DIR="$ROOT/media/.demo_video_tmp"

rm -rf "$TMP_DIR"
mkdir -p "$TMP_DIR"

if [ ! -s "$ROOT/reports/terminal-transcript.txt" ]; then
  python3 "$ROOT/scripts/run_handoff_copilot.py" >/dev/null
fi

make_screenshot_slide() {
  local src="$1"
  local title="$2"
  local subtitle="$3"
  local out="$4"
  magick "$src" \
    -resize 1920x \
    -crop 1920x1080+0+0 +repage \
    -fill "#000000B8" -draw "rectangle 0,810 1920,1080" \
    -font "$FONT" -fill white -pointsize 58 -annotate +72+900 "$title" \
    -font "$FONT" -fill white -pointsize 34 -annotate +72+980 "$subtitle" \
    "$out"
}

make_text_slide() {
  local title="$1"
  local subtitle="$2"
  local body="$3"
  local out="$4"
  magick -size 1920x1080 xc:"#f5f7fb" \
    -fill "#6941c6" -draw "rectangle 0,0 1920,260" \
    -fill "#ffffff" -font "$FONT" -pointsize 72 -annotate +82+150 "$title" \
    -fill "#f1ecff" -font "$FONT" -pointsize 34 -annotate +86+218 "$subtitle" \
    -fill "#ffffff" -stroke "#d8e0ea" -strokewidth 3 -draw "roundrectangle 120,410 1800,760 24,24" \
    -stroke none -fill "#1f2937" -font "$FONT" -pointsize 46 -annotate +170+520 "$body" \
    -fill "#667085" -font "$FONT" -pointsize 28 -annotate +170+640 "The agent is useful because another human or AI can resume from the packet." \
    "$out"
}

make_terminal_slide() {
  local out="$1"
  magick -size 1920x1080 xc:"#0b1220" \
    -fill "#1f2937" -draw "roundrectangle 90,80 1830,980 18,18" \
    -fill "#111827" -draw "rectangle 90,80 1830,148" \
    -fill "#f8fafc" -font "$FONT" -pointsize 30 -annotate +130+124 "CASE-M365-HANDOFF-004 · handoff terminal run" \
    -fill "#bfdbfe" -font "$MONO_FONT" -pointsize 30 -annotate +130+220 "$ python3 microsoft-agent-academy/scripts/run_handoff_copilot.py" \
    -fill "#dbeafe" -font "$MONO_FONT" -pointsize 28 -annotate +130+285 "[packet] required fields captured: case_id, ticket_id, evidence_ids" \
    -fill "#dbeafe" -font "$MONO_FONT" -pointsize 28 -annotate +130+340 "[packet] draft_response, approval_required, blocked_action, cost_summary" \
    -fill "#bbf7d0" -font "$MONO_FONT" -pointsize 28 -annotate +130+410 "[quality] handoff_completeness=1.0" \
    -fill "#bbf7d0" -font "$MONO_FONT" -pointsize 28 -annotate +130+465 "[resume] resumable_by_next_actor=True" \
    -fill "#fde68a" -font "$MONO_FONT" -pointsize 28 -annotate +130+535 "[approval] customer-facing send remains blocked until manager approval" \
    -fill "#93c5fd" -font "$MONO_FONT" -pointsize 28 -annotate +130+605 "[boundary] verified local handoff agent; no live Copilot Studio execution claimed" \
    "$out"
}

cat > "$TMP_DIR/narration.txt" <<'TEXT'
Human-AI Handoff Copilot is a Microsoft Agent Academy prototype for a simple but important idea: the best agents are not the ones that pretend to finish everything alone.

The best agents know when to hand work to a human, what evidence to preserve, and how the next person or AI can safely resume.

This demo runs a local support case. A Copilot-style agent retrieves policy, checks the worklog, drafts a customer response, then blocks the customer-facing send because the answer is financial and needs manager approval.

The product creates a handoff packet with required fields, evidence IDs, a draft response, cost summary, blocked action, resume instructions, and a hash of the packet state.

The resume proof shows the handoff is complete: no required fields are missing, the next actor can resume, and the risky action remains blocked.

The repository also includes Copilot Studio-ready instructions, action contracts, and an adaptive approval card. This is a verified local prototype, not a claim of live Copilot Studio execution.
TEXT

"$EDGE_TTS_PYTHON" -m edge_tts \
  --voice "$EDGE_TTS_VOICE" \
  --rate="$EDGE_TTS_RATE" \
  --file "$TMP_DIR/narration.txt" \
  --write-media "$TMP_DIR/narration.mp3"

make_text_slide \
  "Human-AI Handoff Copilot" \
  "A Copilot-style workflow for safe human-agent continuity" \
  "Good agents know when to pause, preserve, and transfer control." \
  "$TMP_DIR/slide-0.png"

make_terminal_slide "$TMP_DIR/slide-1.png"

make_screenshot_slide "$ROOT/media/handoff-copilot-architecture-full.png" \
  "Handoff Architecture" \
  "Evidence, approval, cost, and resume instructions stay visible." \
  "$TMP_DIR/slide-2.png"

make_screenshot_slide "$REPO_ROOT/shared-agentops-engine/media/shared-dashboard-full.png" \
  "AgentOps Timeline" \
  "Human, AI, API, risk, and approval events are reviewable together." \
  "$TMP_DIR/slide-3.png"

make_text_slide \
  "Copilot Studio-Ready Assets" \
  "Instructions, action contracts, and an adaptive approval card" \
  "The local prototype is packaged for a Microsoft agent implementation path." \
  "$TMP_DIR/slide-4.png"

make_screenshot_slide "$ROOT/media/handoff-copilot-architecture-full.png" \
  "Honest Submission Boundary" \
  "Verified local handoff agent. Live Copilot Studio execution is not claimed yet." \
  "$TMP_DIR/slide-5.png"

ffmpeg -y \
  -loop 1 -t 14 -i "$TMP_DIR/slide-0.png" \
  -loop 1 -t 14 -i "$TMP_DIR/slide-1.png" \
  -loop 1 -t 14 -i "$TMP_DIR/slide-2.png" \
  -loop 1 -t 14 -i "$TMP_DIR/slide-3.png" \
  -loop 1 -t 14 -i "$TMP_DIR/slide-4.png" \
  -loop 1 -t 14 -i "$TMP_DIR/slide-5.png" \
  -i "$TMP_DIR/narration.mp3" \
  -filter_complex "[0:v][1:v][2:v][3:v][4:v][5:v]concat=n=6:v=1:a=0,format=yuv420p[v];[6:a]loudnorm=I=-16:TP=-1.5:LRA=11,volume=0.85[a]" \
  -map "[v]" -map "[a]" -r 30 -shortest -movflags +faststart "$OUT"

cp "$OUT" "$LEGACY_OUT"
rm -rf "$TMP_DIR"
echo "$OUT"
