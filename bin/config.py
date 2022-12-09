feeds = { "sources": 
    [
        {
            "name": "CoinBlocker",
            "url": "https://zerodot1.gitlab.io/CoinBlockerLists/list.txt",
            "type": ["domain"],
            "regex": "N/A"
        },
        {
            "name": "blocklist.de-all",
            "url": "https://lists.blocklist.de/lists/all.txt",
            "type": ["ip"],
            "regex": "N/A"
        },
        {
            "name": "OpenPhish",
            "url": "https://openphish.com/feed.txt",
            "type": ["url"],
            "regex": "N/A"
        },
        {
            "name": "dan.me TOR Exit Nodes",
            "url": "https://www.dan.me.uk/torlist/",
            "type": ["ip"],
            "regex": "N/A"
        },
        {
            "name": "Greensnow",
            "url": "http://blocklist.greensnow.co/greensnow.txt",
            "type": ["ip"],
            "regex": "N/A"
        },
        {
            "name": "Botvrij.eu - ips",
            "url": "http://www.botvrij.eu/data/ioclist.ip-dst.raw",
            "type": ["ip"],
             "regex": "N/A"
        },
        {
            "name": "URLHause abuse.ch",
            "url": "https://urlhaus.abuse.ch/downloads/text/",
            "type": ["url"],
            "regex": "N/A"
        },
        {
            "name": "Brute force Blockers",
            "url": "http://danger.rulez.sk/projects/bruteforceblocker/blist.php",
            "type": ["ip"],
            "regex": "(\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3})"
        },
        {
            "name": "Alienvault",
            "url": "http://reputation.alienvault.com/reputation.data",
            "type": ["ip"],
            "regex": "^(.*?)\#"
        },
        {
            "name": "CI Bad Guys",
            "url": "http://cinsscore.com/list/ci-badguys.txt",
            "type": ["ip"],
            "regex": "N/A"
        },
        {
            "name": "Emerging Threats",
            "url": "https://rules.emergingthreats.net/blockrules/compromised-ips.txt",
            "type": ["ip"],
            "regex": "N/A"
        },
        {
            "name": "Darklist",
            "url": "https://www.darklist.de/raw.php",
            "type": ["ip"],
            "regex": "N/A"
        },
        {
            "name": "SSH dictonary Attacks",
            "url": "https://charles.the-haleys.org/ssh_dico_attack_hdeny_format.php/hostsdeny.txt",
            "type": ["ip"],
            "regex": "(\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3})"
        },
        {
            "name": "SSL BL - abuse.ch",
            "url": "https://sslbl.abuse.ch/blacklist/sslipblacklist.csv",
            "type": ["ip"],
            "regex": "(\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3})"
        },
        {
            "name": "Talos IP Blacklist",
            "url": "http://www.talosintelligence.com/documents/ip-blacklist",
            "type": ["ip"],
            "regex": "N/A"
        },
        {
            "name": "PhishTank",
            "url": "http://data.phishtank.com/data/online-valid.csv",
            "type": ["url"],
            "regex": "^.*?\,(.*?)\,"
        }
    ]
}