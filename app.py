from faster_whisper import WhisperModel

model = WhisperModel("large", device="cpu", compute_type="int8")

segments, info = model.transcribe(
    "teksti.mp3",
    language="fi" 
)

print("\n--- TXT ---\n")

full_text = ""
for segment in segments:
    print(segment.text)
    full_text += segment.text + " "

with open("litterointi.txt", "w", encoding="utf-8") as f:
    f.write(full_text)
