import subprocess
import json

acts = [
    {
        "id": "act1_voice",
        "text": "在辽阔的交界地，无上意志赐予黄金树繁盛荣光。永恒女王玛莉卡统御众生，命定之死被封印于黑剑体内，不朽的黄金律法就此建立。",
    },
    {
        "id": "act2_voice",
        "text": "然而暗流涌动。月之公主菈妮盗走死亡卢恩，黑刀刺客暗杀了黄金之子葛德文。陷入绝望的女王举起石槌，彻底砸碎了艾尔登法环。",
    },
    {
        "id": "act3_voice",
        "text": "法环崩解为大卢恩碎片，诸位半神展开惨烈的破碎战争。碎星拉塔恩与女武神玛莲妮亚决战盖利德，猩红腐败将大地化作焦土。",
    },
    {
        "id": "act4_voice",
        "text": "无上意志抛弃了半神，微弱的赐福重新唤醒被放逐的褪色者。在指头女巫梅琳娜的引导下，褪色者跨越雾海，踏上争夺法环的征程。",
    },
    {
        "id": "act5_voice",
        "text": "燃烧黄金树，直面艾尔登之兽。是修复法环成为艾尔登之王，追随菈妮开启群星时代，还是化身癫火焚尽世间？交界地的命运由你抉择。",
    }
]

durations = {}
for act in acts:
    act_id = act["id"]
    aiff_path = f"assets/{act_id}.aiff"
    mp3_path = f"assets/{act_id}.mp3"
    subprocess.run(["say", "-v", "Tingting", "-r", "180", act["text"], "-o", aiff_path], check=True)
    subprocess.run(["ffmpeg", "-y", "-i", aiff_path, "-af", "volume=1.3", mp3_path], capture_output=True, check=True)
    probe = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", mp3_path], capture_output=True, text=True)
    dur = float(json.loads(probe.stdout)["format"]["duration"])
    durations[act_id] = dur
    print(f"{act_id}: {dur:.2f}s")

with open("assets/audio_durations.json", "w") as f:
    json.dump(durations, f, indent=2)
print("Finished voice generation.")
