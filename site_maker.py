import pandas as pd

# Carrega o DataFrame combinado
site_df = pd.read_csv("site_metadata.csv")

# Começa a montagem da tabela HTML
lines = []
lines.append("<table>")
lines.append("  <tr>")
lines.append("    <th>ID</th>")
lines.append("    <th>Speech</th>")
lines.append("    <th>Ground Truth</th>")
lines.append("    <th>YourTTS CP (CMLTTS Pre-Train)</th>")
lines.append("    <th>YourTTS Sim</th>")
lines.append("    <th>F5TTS CP (CommonVoice Pre-Train)</th>")
lines.append("    <th>F5TTS Sim</th>")
lines.append("  </tr>")

# Preenche a tabela linha a linha
for idx, row in site_df.iterrows():
    audio_name = row["audio_file"]
    transcription = row["transcription"]
    
    gt_path = f"{{{{ 'experiments/ground_truth/{audio_name}' }}}}"
    yt_audio = f"sr16k_mono_{audio_name}_synthesized.wav"
    f5_audio = f"fn-cv_{audio_name}"
    
    yt_path = f"{{{{ 'yt-fn-cml/{yt_audio}' }}}}"
    f5_path = f"{{{{ 'f5-fn-cv/{f5_audio}' }}}}"

    row_html = f"""
<tr>
  <td>{idx+1:02}</td>
  <td>{transcription}</td>
  <td><audio controls preload style="width: 150px; height:40px;"><source src="{gt_path}" type="audio/mpeg"></audio></td>
  <td><audio controls preload style="width: 150px; height:40px;"><source src="{yt_path}" type="audio/mpeg"></audio></td>
  <td>{row["sr16k_mono"]}</td>
  <td><audio controls preload style="width: 150px; height:40px;"><source src="{f5_path}" type="audio/mpeg"></audio></td>
  <td>{row["cv-fn"]}</td>
</tr>"""
    lines.append(row_html.strip())

lines.append("</table>")

# Salva a tabela no arquivo .text
with open("site_table.text", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
