🔐 SOC Log Analyzer (Python)

A Python-based log analysis tool designed to simulate real-world Security Operations Center (SOC) workflows. This project detects suspicious login activity such as brute-force attacks by parsing authentication logs and generating alerts.

⸻

🚀 Features
	•	📄 Parses authentication log files (auth.log)
	•	🔍 Detects failed login attempts
	•	🌐 Extracts IP addresses using Regular Expressions (Regex)
	•	📊 Counts failed attempts per IP
	•	🚨 Identifies brute-force attacks using threshold-based detection
	•	📝 Generates alerts and saves them to alerts.txt



🧠 How It Works
	1.	Reads log file line by line
	2.	Filters failed login attempts
	3.	Extracts IP addresses from logs
	4.	Counts number of attempts per IP
	5.	Applies threshold logic to detect suspicious activity
	6.	Generates alerts for flagged IPs



📂 Project Structure

soc-log-analyzer/
│
├── auth.log        # Sample log file
├── analyzer.py     # Main script
└── alerts.txt      # Generated alerts




🛠️ Technologies Used
	•	Python 3
	•	Regular Expressions (re)
	•	File Handling


▶️ How to Run
	1.	Clone the repository:

git clone https://github.com/Loke31033/SOC-log-analyzer.git

	2.	Navigate to the project folder:

cd SOC-log-analyzer

	3.	Run the script:

python analyzer.py


📊 Sample Output

Failed Login Summary:

192.168.1.10 → 3 attempts
172.16.0.2 → 2 attempts

Suspicious IPs:

ALERT: 192.168.1.10 → 3 failed attempts



🎯 Use Case

This project demonstrates how SOC analysts:
	•	Monitor authentication logs
	•	Detect brute-force attacks
	•	Identify suspicious IP activity
	•	Automate alert generation



📈 Future Enhancements
	•	Integrate Threat Intelligence APIs (VirusTotal, AbuseIPDB)
	•	Add real-time log monitoring
	•	Email/Slack alert integration
	•	Dashboard visualization

👨‍💻 Author

Lokeshwar V
🔗 GitHub: https://github.com/Loke31033
🔗 LinkedIn: https://www.linkedin.com/in/lokeshwar-v-011b20289
