import subprocess
from datetime import datetime

def detect_vpn_abuse():
    """Flag unusual peer behavior"""
    sessions = subprocess.check_output(["wg", "show", "all", "transfer"])
    for line in sessions.decode().split('\n'):
        peer, rx, tx, last_handshake = line.split()
        if int(rx) > 10_000_000:  # >10MB download
            alert(f"Data exfiltration detected from {peer}")
        if (datetime.now() - datetime.fromisoformat(last_handshake)).days > 30:
            revoke_peer(peer)  # Auto-revoke stale peers

def revoke_peer(peer_pubkey):
    subprocess.run(["wg", "set", "wg0", "peer", peer_pubkey, "remove"])
