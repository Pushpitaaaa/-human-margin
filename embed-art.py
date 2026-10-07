#!/usr/bin/env python3
"""Pack the art/ folder into ONE html file (data URIs), for publishing or sharing a single file.
Usage: python3 embed-art.py index.html index-with-art.html
"""
import base64, json, mimetypes, os, sys
src, out = sys.argv[1], sys.argv[2]
folder = os.path.join(os.path.dirname(os.path.abspath(src)), 'art')
slots = {}
for name in ['bg','mid','fg','mimi','figurine']:
    for ext in ['webp','png','jpg']:
        f = os.path.join(folder, f'{name}.{ext}')
        if os.path.exists(f):
            mime = mimetypes.guess_type(f)[0] or 'image/png'
            slots[name] = f'data:{mime};base64,' + base64.b64encode(open(f,'rb').read()).decode()
            break
audio_folder = os.path.join(os.path.dirname(os.path.abspath(src)), 'audio')
sounds = {}
for name in ['hum','slide','tick','rustle','car','launch']:
    for ext in ['mp3','ogg','wav']:
        f = os.path.join(audio_folder, f'{name}.{ext}')
        if os.path.exists(f):
            mime = mimetypes.guess_type(f)[0] or 'audio/mpeg'
            sounds[name] = f'data:{mime};base64,' + base64.b64encode(open(f,'rb').read()).decode()
            break
html = open(src, encoding='utf-8').read()
tag = '<script>window.HM_ART=' + json.dumps(slots) + ';window.HM_AUDIO=' + json.dumps(sounds) + ';</script>\n'
html = html.replace('<script>\n(function(){', tag + '<script>\n(function(){', 1)
open(out, 'w', encoding='utf-8').write(html)
print('embedded art:', ', '.join(slots) or 'none', '| sounds:', ', '.join(sounds) or 'none', '->', out)
