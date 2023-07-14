from tkinter import *
import os

root = Tk()
root.state("zoomed")

bg = PhotoImage( file = "bg.png")
logo = PhotoImage( file = "logo.png")
  
label1 = Label( root, image = bg)
label1.place(x = 0,y = 0)

labellogo = Label( root, image = logo)
labellogo.place(in_=label1, relx = 0.70, rely = 0.02)

labelinfo = Label( root, text="Done by: \n Kethamreddy Karthikeya Reddy \n CH.EN.U4CYS20038 \n Amrita School Of Computing")
labelinfo.place(in_=label1, relx = 0.87, rely = 0.9)

label2 = Label( root, text = "Forensics Tools", font =("Arial", 32))
label2.place(x = 0, anchor = "center")
label2.pack(pady = 50)
  
frame1 = Frame(root)
v1 = Scrollbar(frame1)
v1.pack(side = RIGHT, fill = Y)
t1 = Text(frame1, width = 50, height = 15, wrap = WORD, yscrollcommand = v1.set)
t1.tag_configure("tag_name", justify='center')
t1.insert('1.0',        
         'Digital Security'
         '\n\n\n \t Digital security, also known as cybersecurity, refers to the measures and practices taken to protect computer systems, networks, and data from unauthorized access, use, disclosure,' 
         'disruption, modification, or destruction. It is essential to ensure the confidentiality, integrity, and availability of digital information. Here are some basic concepts of digital '
         'security: \n\n \t Passwords: Use strong, unique passwords for all your online accounts. Avoid using easily guessable information such as your name, birthdate, or common words. Consider using '
         'a password manager to generate and store complex passwords securely.'
         '\n\n \t Two-Factor Authentication (2FA): Enable 2FA whenever possible. It provides an extra layer of security by requiring a second form of verification, such as a code sent to your '
         'mobile device, in addition to your password.'
         '\n\n \t Software Updates: Keep your operating system, applications, and antivirus software up to date. Software updates often include important security patches that address '
         'vulnerabilities and protect against emerging threats.'
         '\n\n \t Secure Browsing: Be cautious when sharing personal information online. Look for the padlock icon and "https" in the URL to ensure a secure connection. Avoid clicking on '
         'suspicious links or downloading files from untrusted sources.'
         '\n\n \t Firewalls: Use a firewall to monitor and control incoming and outgoing network traffic. Firewalls help prevent unauthorized access to your computer or network by blocking '
         'potentially harmful connections.'
         '\n\n \t Antivirus Software: Install reputable antivirus software to detect and remove malware from your devices. Regularly scan your system for viruses, trojans, and other malicious '
         'software.'
         '\n\n \t Data Backup: Regularly backup your important files and data to an external storage device or a cloud-based service. In case of data loss or ransomware attacks, backups can help '
         'restore your information.'
         '\n\n \t Email and Phishing: Be cautious when opening email attachments or clicking on links, especially if they are unsolicited or from unknown sources. Phishing attacks often occur via '
         'email and aim to trick you into revealing sensitive information or downloading malware.'
         '\n\n \t Social Engineering: Be aware of social engineering techniques where attackers manipulate individuals into divulging confidential information. Exercise caution when sharing '
         'personal or financial details over the phone or online.'
         '\n\n \t Privacy Settings: Review and adjust the privacy settings on your social media accounts, applications, and online services. Limit the amount of personal information you share '
         'publicly.')
t1.tag_add("tag_name", "1.0", "end")
t1.config(state='disabled')
t1.pack(side=TOP, fill=X)
v1.config(command=t1.yview)

frame2 = Frame(root)
v2 = Scrollbar(frame2)
v2.pack(side = RIGHT, fill = Y)
t2 = Text(frame2, width = 50, height = 15, wrap = WORD, yscrollcommand = v2.set)
t2.tag_configure("tag_name", justify='center')
t2.insert('1.0',  
          'Authentication and Authorization'
          '\n\n\n Authentication and authorization are two fundamental concepts in digital security that play a crucial role in controlling access to resources and ensuring the security of '
          "computer systems and networks. Here's an overview of these concepts:"
          "\n\n \t Authentication:"
          'Authentication is the process of verifying the identity of a user, device, or system entity attempting to access a resource or service. It ensures that the entity claiming an '
          'identity is indeed who they say they are. The most common form of authentication is the use of usernames and passwords, but there are also other methods such as biometric '
          'authentication (fingerprint or face recognition), smart cards, tokens, and digital certificates.'
          '\n\n \t Authorization:'
          'Authorization is the process of granting or denying access rights and permissions to authenticated users or entities based on their identity and the privileges they possess. It '
          'determines what actions or resources a user is allowed to access or perform within a system. Authorization is typically based on user roles, group memberships, or specific '
          'permissions assigned to individual accounts.'
          '\n\n In summary, authentication verifies the identity of a user or entity, while authorization determines what actions and resources that authenticated user or entity is allowed '
          'to access or perform. To illustrate the relationship between authentication and authorization, consider a scenario where a user wants to access a secure online banking application:'
          '\n\n Authentication: The user enters their username and password to authenticate themselves to the system. The system verifies the entered credentials against the stored '
          'credentials to determine if the user is who they claim to be.'
          "\n\n Authorization: Once authenticated, the system checks the user's authorization level or role (e.g., customer, teller, or administrator) to determine what actions and resources "
          'the user is allowed to access. For example, a customer may be authorized to view account balances and make transfers, while a teller may be authorized to perform additional tasks '
          'such as depositing or withdrawing money.'
          '\n\n By combining authentication and authorization, systems can ensure that only legitimate users with appropriate privileges can access sensitive information and perform authorized '
          'actions, helping to maintain the security and integrity of the system.')

t2.tag_add("tag_name", "1.0", "end")
t2.config(state='disabled')
t2.pack(side=TOP, fill=X)
v2.config(command=t2.yview)

frame3 = Frame(root)
v3 = Scrollbar(frame3)
v3.pack(side = RIGHT, fill = Y)
t3 = Text(frame3, width = 50, height = 15, wrap = WORD, yscrollcommand = v3.set)
t3.tag_configure("tag_name", justify='center')
t3.insert('1.0',        
         'The Internet and the HTTP Protocol'
         '\n\n\n The internet is a global network of interconnected computers and devices that communicate with each other using a set of standardized protocols. It enables the exchange of'
         "information and facilitates various online services and activities. One of the key protocols used on the internet is the Hypertext Transfer Protocol (HTTP). Here's an overview of "
         "the internet and the HTTP protocol:"
         "\n\n \t The Internet: The internet is a vast network infrastructure that connects millions of devices worldwide. It allows for the transmission of data packets between computers "
         'and facilitates communication and the sharing of resources. The internet operates on the basis of the Internet Protocol Suite (TCP/IP), which provides a set of rules for data '
         'transmission and addressing.'
         '\n\n \t HTTP (Hypertext Transfer Protocol):'
         'HTTP is the protocol used for communication between web browsers and web servers. It is the foundation of the World Wide Web (WWW) and enables the retrieval of resources, such as '
         'web pages, images, videos, and other content, from servers to browsers.'
         '\n\n When you enter a URL (Uniform Resource Locator) into your web browser, such as http://www.example.com, the browser initiates an HTTP request to the web server hosting that URL.'
         'The server responds by sending back an HTTP response, which contains the requested resource or an error message if the resource is not found. HTTP operates on a client-server model,'
         'where the client (typically a web browser) sends requests to the server, and the server processes the requests and sends back the appropriate responses. The requests and responses '
         'are structured in a specific format, including headers and optional message bodies.'
         '\n\n \t HTTPS (Hypertext Transfer Protocol Secure):'
         'HTTPS is an extension of HTTP that adds a layer of encryption and security to the communication between the client and the server. It uses SSL (Secure Sockets Layer) or TLS '
         '(Transport Layer Security) protocols to encrypt data and protect it from unauthorized access or tampering. HTTPS is commonly used for secure transactions, such as online banking, '
         'e-commerce, and sensitive data transfers.'
         "\n\n The use of HTTPS is indicated by a padlock icon in the browser's address bar, and the URL begins with 'https://' instead of 'http://'. HTTPS provides authentication of the "
         "server's identity and ensures the confidentiality and integrity of data transmitted over the network."
         "\n\n In summary, the internet is a global network infrastructure that enables communication and the exchange of information. HTTP is the protocol that governs the communication "
         "between web browsers and servers, while HTTPS adds encryption and security to the communication. These protocols are foundational to the functioning of the World Wide Web and"
         'enable the retrieval and delivery of web resources.')
t3.tag_add("tag_name", "1.0", "end")
t3.config(state='disabled')
t3.pack(side=TOP, fill=X)
v3.config(command=t3.yview)

frame4 = Frame(root)
v4 = Scrollbar(frame4)
v4.pack(side = RIGHT, fill = Y)
t4 = Text(frame4, width = 50, height = 15, wrap = WORD, yscrollcommand = v4.set)
t4.tag_configure("tag_name", justify='center')
t4.insert('1.0',        
         'Networking Protocols'
         '\n\n\n Networking protocols are sets of rules and conventions that govern how devices communicate and exchange data within a computer network. These protocols define the format, '
         'structure, and behavior of data packets, as well as the methods for establishing and terminating network connections. Here are some common networking protocols:'
         '\n\n \t Internet Protocol (IP):'
         'IP is a fundamental protocol used for addressing and routing data packets across the internet. It provides the basis for sending and receiving data between devices. IP version 4 '
         '(IPv4) and IP version 6 (IPv6) are the two main versions of this protocol.'
         '\n\n \t Transmission Control Protocol (TCP):'
         'TCP is a reliable, connection-oriented protocol that operates on top of IP. It ensures the reliable delivery of data by establishing a connection, breaking the data into packets, '
         'numbering them, and reassembling them at the destination. TCP handles flow control, error recovery, and congestion control.'
         '\n\n \t User Datagram Protocol (UDP):'
         'UDP is a lightweight, connectionless protocol that operates on top of IP. It provides a simple mechanism for sending datagrams (packets) without establishing a connection. UDP is '
         'used in applications where real-time data delivery is more critical than reliability, such as streaming media or online gaming.'
         '\n\n \t Internet Control Message Protocol (ICMP):'
         'ICMP is a protocol used for error reporting, diagnostic messages, and network management. It is primarily used by network devices, such as routers and hosts, to communicate '
         'network-related information and report errors.'
         '\n\n \t Border Gateway Protocol (BGP):'
         'BGP is the protocol used for routing between autonomous systems (AS) in the internet. It determines the best path for forwarding packets between different networks and enables the '
         'exchange of routing information among routers.'
         '\n\n \t Domain Name System (DNS):'
         'DNS is a protocol that translates domain names (e.g., www.example.com) into IP addresses. It enables users to access resources on the internet using human-readable domain names '
         'instead of numeric IP addresses.'
         '\n\n \t Simple Mail Transfer Protocol (SMTP):'
         'SMTP is a protocol for sending and receiving email messages. It defines the rules for email transfer between mail servers and specifies how email clients interact with mail servers'
         'to send and receive messages.'
         '\n\n \t File Transfer Protocol (FTP):'
         'FTP is a protocol for transferring files between computers over a network. It provides a standard set of commands and responses for uploading, downloading, and managing files on '
         'remote servers.'
         '\n\n These are just a few examples of networking protocols. There are many other protocols used for specific purposes, such as HTTP for web browsing, SSH for secure remote access, '
         'and SNMP for network management. Different protocols work together to enable the smooth functioning and communication within computer networks.')
t4.tag_add("tag_name", "1.0", "end")
t4.config(state='disabled')
t4.pack(side=TOP, fill=X)
v4.config(command=t4.yview)

frame5 = Frame(root)
v5 = Scrollbar(frame5)
v5.pack(side = RIGHT, fill = Y)
t5 = Text(frame5, width = 50, height = 15, wrap = WORD, yscrollcommand = v5.set)
t5.tag_configure("tag_name", justify='center')
t5.insert('1.0',        
         'Cyber Attacks'
         '\n\n\n Cyber attacks refer to malicious activities carried out by individuals or groups with the intent to compromise computer systems, networks, or digital information. These '
         'attacks can have various motivations, including financial gain, political agendas, espionage, or disruption of services. Here are some common types of cyber attacks:'
         '\n\n \t Malware: Malware, short for malicious software, refers to any software designed to harm, exploit, or gain unauthorized access to a computer system. This includes viruses, '
         'worms, Trojans, ransomware, spyware, and adware. Malware can be spread through email attachments, infected websites, or compromised software.'
         '\n\n \t Phishing: Phishing attacks involve fraudulent attempts to deceive individuals into revealing sensitive information, such as usernames, passwords, credit card details, or '
         'social security numbers. Attackers often masquerade as trustworthy entities, such as banks or popular websites, and use email, instant messaging, or deceptive websites to trick victims.'
         '\n\n \t Denial of Service (DoS) and Distributed Denial of Service (DDoS): DoS and DDoS attacks aim to overwhelm a target system or network with a flood of traffic, rendering it'
         'unavailable to legitimate users. DoS attacks are launched from a single source, while DDoS attacks involve multiple sources, often utilizing botnets to orchestrate the attack.'
         '\n\n \t Man-in-the-Middle (MitM) Attacks: MitM attacks involve intercepting and altering communication between two parties without their knowledge. Attackers position themselves '
         'between the communicating parties and can eavesdrop, modify, or inject malicious content into the communication.'
         "\n\n \t SQL Injection: SQL injection attacks exploit vulnerabilities in web applications that allow attackers to inject malicious SQL code into the application's database. This can"
         'result in unauthorized access, data theft, or manipulation of the database.'
         '\n\n \t Social Engineering: Social engineering attacks manipulate human psychology to deceive individuals and gain access to sensitive information. Examples include impersonation, '
         'pretexting, baiting, or phishing calls to extract confidential data or convince individuals to perform certain actions.'
         '\n\n \t Zero-day Exploits: Zero-day exploits target vulnerabilities in software or systems that are unknown to the vendor or developers. Attackers take advantage of these'
         'vulnerabilities before a patch or fix is available, increasing the risk of successful attacks.'
         '\n\n \t Insider Threats: Insider threats involve individuals within an organization who abuse their access privileges to steal or leak sensitive data, compromise systems, or '
         'disrupt operations. This can be intentional or unintentional.'
         '\n\n Preventing and mitigating cyber attacks require a combination of technical measures and user awareness. This includes implementing strong security measures, regularly updating '
         'software, employing firewalls and intrusion detection systems, conducting security audits, educating users about safe online practices, and having incident response plans in place.'
         "It's important to stay vigilant and keep up with the latest security practices to protect against evolving cyber threats.")
t5.tag_add("tag_name", "1.0", "end")
t5.config(state='disabled')
t5.pack(side=TOP, fill=X)
v5.config(command=t5.yview)

frame6 = Frame(root)
v6 = Scrollbar(frame6)
v6.pack(side = RIGHT, fill = Y)
t6 = Text(frame6, width = 50, height = 15, wrap = WORD, yscrollcommand = v6.set)
t6.tag_configure("tag_name", justify='center')
t6.insert('1.0',        
         'Digital Privacy'
         '\n\n\n \t Data privacy refers to the protection and appropriate handling of personal information, ensuring that individuals have control over how their data is collected, used, and '
         'shared. It involves safeguarding sensitive data from unauthorized access, disclosure, alteration, or destruction. Here are some key aspects of data privacy:'
         '\n\n \t Personal Data: Personal data includes any information that can identify an individual, such as names, addresses, phone numbers, social security numbers, email addresses, '
         'financial details, medical records, and online identifiers. Data privacy emphasizes the need to handle personal data securely and responsibly.'
         '\n\n \t Consent: Obtaining informed and explicit consent from individuals before collecting and processing their personal data is a fundamental aspect of data privacy. Consent should be '
         'freely given, specific, and based on clear and easily understandable information about how the data will be used.'
         '\n\n \t Data Collection and Purpose Limitation: Organizations should collect only the necessary data required for a specific purpose and should not retain it for longer than necessary. '
         'Limiting the collection and storage of personal data helps minimize risks and potential harm associated with data breaches.'
         '\n\n \t Security Measures: Implementing appropriate security measures is crucial to protect personal data from unauthorized access, loss, or theft. This includes using encryption, access '
         'controls, firewalls, secure networks, and regular security audits to ensure the integrity and confidentiality of personal data.'
         '\n\n \t Data Sharing and Third Parties: When sharing personal data with third parties, organizations should have agreements and safeguards in place to ensure that the data is handled '
         'securely and in compliance with privacy laws. This includes assessing the privacy practices of third parties and ensuring they adhere to similar data protection standards.'
         '\n\n \t User Rights: Data privacy regulations often grant individuals certain rights regarding their personal data. These rights may include the right to access, correct, delete, or '
         'restrict the processing of their data. Organizations should provide mechanisms for individuals to exercise these rights and respond to their requests in a timely manner.'
         '\n\n \t Privacy Policies: Organizations should have clear and transparent privacy policies that outline how they collect, use, and protect personal data. Privacy policies should be easily '
         'accessible and written in a clear and understandable language.'
         '\n\n \t Compliance with Privacy Regulations: Data privacy is governed by various laws and regulations, such as the General Data Protection Regulation (GDPR) in the European Union and the '
         'California Consumer Privacy Act (CCPA) in the United States. Organizations should ensure compliance with applicable privacy regulations and establish internal processes to handle'
         'data privacy concerns and incidents.'
         '\n\n \t Protecting data privacy is a shared responsibility between individuals, organizations, and regulatory bodies. By adopting privacy-focused practices and technologies, respecting '
         'user consent, and implementing robust security measures, data privacy can be upheld, promoting trust and confidence in the handling of personal information.')
t6.tag_add("tag_name", "1.0", "end")
t6.config(state='disabled')
t6.pack(side=TOP, fill=X)
v6.config(command=t6.yview)

frame7 = Frame(root)
v7 = Scrollbar(frame7)
v7.pack(side = RIGHT, fill = Y)
t7 = Text(frame7, width = 50, height = 15, wrap = WORD, yscrollcommand = v7.set)
t7.tag_configure("tag_name", justify='center')
t7.insert('1.0',        
         'Preventing Attacks and Breaches'
         '\n\n\n \t Preventing attacks and breaches requires the implementation of various security controls and best practices. Here are some key measures that can help enhance security and'
         'mitigate the risk of attacks:'
         '\n\n \t Network Security:'
         '\n Firewalls: Implement firewalls to control incoming and outgoing network traffic, blocking unauthorized access and protecting against external threats.'
         '\n Intrusion Detection and Prevention Systems (IDPS): Use IDPS to monitor network activities and detect and prevent suspicious or malicious activities.'
         '\n\n \t Strong Authentication and Access Controls:'
         '\n User Authentication: Enforce strong password policies and consider implementing multi-factor authentication (MFA) for user accounts to add an extra layer of security.'
         '\n User Access Controls: Implement role-based access controls (RBAC) to ensure that users have appropriate access privileges based on their roles and responsibilities.'
         '\n\n \t Regular Software Updates and Patch Management:'
         'Keep all software, including operating systems, applications, and firmware, up to date with the latest security patches and updates to address known vulnerabilities.'
         '\n\n \t Encryption:'
         '\n Encrypt sensitive data both in transit (using protocols like HTTPS, SSL/TLS) and at rest (on storage devices) to protect data from unauthorized access or interception.'
         '\n\n \t Employee Education and Awareness:'
         '\n Conduct regular security awareness training for employees to educate them about common attack vectors, phishing techniques, and best practices for data protection.'
         '\n\n \t Incident Response Planning:'
         '\n Develop an incident response plan to effectively respond to security incidents and minimize the impact of a breach. This includes establishing clear procedures for detecting, '
         'reporting, and containing security incidents, as well as communicating with stakeholders.'
         '\n\n \t Data Backup and Recovery:'
         '\n Regularly back up critical data and verify the integrity of backups. This helps mitigate the impact of data loss or ransomware attacks by restoring systems and data to a known '
         'secure state.'
         '\n\n \t Vulnerability Management:'
         '\n Conduct regular vulnerability assessments and penetration testing to identify and remediate security vulnerabilities in systems and applications.'
         '\n\n \t Security Monitoring and Logging:'
         '\n Implement robust logging mechanisms to track and monitor system activities, enabling the detection of anomalous behavior or potential security breaches.'
         '\n\n \t Vendor and Third-Party Risk Management:'
         '\n Assess the security practices of vendors and third-party providers that have access to your systems or handle your data, ensuring they meet your security requirements.'
         "\n It's important to note that security is an ongoing process, and a layered approach that combines multiple security controls is often the most effective. Regular risk assessments,"
         'security audits, and staying updated on emerging threats and best practices are essential for maintaining a strong security posture.')
t7.tag_add("tag_name", "1.0", "end")
t7.config(state='disabled')
t7.pack(side=TOP, fill=X)
v7.config(command=t7.yview)

frame8 = Frame(root)
v8 = Scrollbar(frame8)
v8.pack(side = RIGHT, fill = Y)
t8 = Text(frame8, width = 50, height = 15, wrap = WORD, yscrollcommand = v8.set)
t8.tag_configure("tag_name", justify='center')
t8.insert('1.0',        
         'Compilance Standards'
         '\n\n\n \t Compliance standards are guidelines and regulations that organizations must adhere to in order to meet specific legal, regulatory, or industry requirements. These '
         'standards help ensure that organizations maintain appropriate levels of security, privacy, and data protection. Here are some common compliance standards:'
         '\n\n \t General Data Protection Regulation (GDPR):'
         'The GDPR is a comprehensive privacy regulation enacted by the European Union (EU) that governs the protection and processing of personal data of EU residents. It imposes obligations'
         'on organizations worldwide that handle EU citizens data and includes requirements for consent, data minimization, data subject rights, breach notification, and privacy by design.'
         '\n\n \t Payment Card Industry Data Security Standard (PCI DSS):'
         'PCI DSS is a set of security standards developed by major credit card companies to protect cardholder data. It applies to organizations that store, process, or transmit credit card '
         'information. Compliance with PCI DSS involves implementing specific security controls, such as network segmentation, encryption, access controls, and regular security assessments.'
         '\n\n \t Health Insurance Portability and Accountability Act (HIPAA):'
         'HIPAA is a U.S. regulation that sets privacy and security standards for protecting individuals health information. It applies to healthcare providers, health plans, and healthcare '
         'clearinghouses. Compliance with HIPAA involves implementing safeguards to protect the confidentiality, integrity, and availability of electronic protected health information (ePHI).'
         '\n\n \t Sarbanes-Oxley Act (SOX):'
         'SOX is a U.S. legislation that establishes requirements for financial reporting and corporate governance of publicly traded companies. It includes provisions related to internal '
         'controls, data retention, and data accuracy to protect against fraud and financial misconduct.'
         '\n\n \t ISO 27001:'
         'ISO 27001 is an international standard that provides a framework for establishing, implementing, maintaining, and continually improving an information security management system'
         '(ISMS). Compliance with ISO 27001 demonstrates a systematic approach to managing security risks and protecting information assets.'
         '\n\n \t NIST Cybersecurity Framework:'
         'The NIST Cybersecurity Framework, developed by the National Institute of Standards and Technology (NIST) in the United States, provides guidelines and best practices for managing '
         'and improving cybersecurity risk. It offers a risk-based approach to identifying, protecting, detecting, responding to, and recovering from cyber threats.'
         '\n\n \t Federal Information Security Management Act (FISMA):'
         'FISMA is a U.S. law that requires federal agencies to develop and implement information security programs to protect government information and systems. It sets requirements for '
         'risk assessment, security controls, incident response, and continuous monitoring.'
         '\n\n \t International Traffic in Arms Regulations (ITAR):'
         'ITAR is a U.S. regulation that controls the export and import of defense-related articles and services. It includes requirements for safeguarding sensitive technical data and '
         'ensuring it is accessed and shared only by authorized parties.'
         '\n\n These are just a few examples of compliance standards, and there are many more specific to different industries and regions. Organizations should identify the applicable standards '
         'for their operations and ensure they have processes and controls in place to meet the requirements. Compliance with these standards helps protect sensitive information, maintain '
         'customer trust, and avoid legal and financial repercussions.')
t8.tag_add("tag_name", "1.0", "end")
t8.config(state='disabled')
t8.pack(side=TOP, fill=X)
v8.config(command=t8.yview)



frame1.place(relx=0.03, rely=0.25)
frame2.place(relx=0.27, rely=0.25)
frame3.place(relx=0.51, rely=0.25)
frame4.place(relx=0.75, rely=0.25)
frame5.place(relx=0.03, rely=0.6)
frame6.place(relx=0.27, rely=0.6)
frame7.place(relx=0.51, rely=0.6)
frame8.place(relx=0.75, rely=0.6)

root.mainloop()