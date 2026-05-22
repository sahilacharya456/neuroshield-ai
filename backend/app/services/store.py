from app.models.domain import Alert, Endpoint, IOC, Incident, User

users = [User(id="USR-1", name="Sahil Khan", email="admin@neuroshield.ai", role="Admin"), User(id="USR-2", name="Ayesha Malik", email="analyst@neuroshield.ai", role="Analyst"), User(id="USR-3", name="Viewer User", email="viewer@neuroshield.ai", role="Viewer")]
alerts = [
    Alert(id="ALT-9001", title="Credential stuffing against VPN gateway", severity="Critical", status="Open", source_ip="185.199.108.44", endpoint="vpn-edge-01", mitre_technique="T1110", risk_score=96, confidence=94, explanation="High failed-login velocity, external ASN risk, and repeated username spray pattern."),
    Alert(id="ALT-9002", title="Suspicious PowerShell encoded command", severity="High", status="Investigating", source_ip="10.8.4.23", endpoint="win-fin-014", mitre_technique="T1059.001", risk_score=84, confidence=89, explanation="Encoded shell execution with child process behavior matching malware staging."),
    Alert(id="ALT-9003", title="Unusual login time for privileged user", severity="Medium", status="Open", source_ip="45.83.64.12", endpoint="idp-core", mitre_technique="T1078", risk_score=68, confidence=81, explanation="Login occurred outside baseline window from untrusted geography."),
]
incidents = [Incident(id="INC-2410", title="VPN brute force campaign", severity="Critical", status="Active", assigned_analyst="Ayesha Malik", affected_assets=["vpn-edge-01", "idp-core"], timeline=["Alert correlated", "Credential access mapped", "Temporary blocklist applied"], remediation="Enforce MFA reset, block source ranges, rotate affected accounts.")]
endpoints = [Endpoint(hostname="vpn-edge-01", os="Ubuntu 22.04", agent_status="Online", health="Degraded", last_seen="2 min ago", risk_score=91), Endpoint(hostname="win-fin-014", os="Windows 11", agent_status="Online", health="Critical", last_seen="1 min ago", risk_score=87)]
iocs = [IOC(id="IOC-1", type="IP", value="185.199.108.44", status="Malicious", confidence=96, linked_incident="INC-2410"), IOC(id="IOC-2", type="Domain", value="updatecdn-security.net", status="Suspicious", confidence=74, linked_incident="INC-2410")]
mitre = [{"behavior":"Brute Force","tactic":"Credential Access","technique":"T1110"},{"behavior":"PowerShell","tactic":"Execution","technique":"T1059.001"},{"behavior":"Valid Accounts","tactic":"Defense Evasion","technique":"T1078"}]
audit_logs = [{"id":"AUD-1","actor":"admin@neuroshield.ai","action":"login","target":"dashboard","result":"success"}]
notifications = [{"id":"NOT-1","title":"Critical brute force campaign", "severity":"Critical", "read":False}]
