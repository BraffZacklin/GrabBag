#!/

def dot_point(commas):
	return '\n\t\t\t\t - '.join(commas.split(', '))

LOGIC = "authentication solutions, firewalls, antivirus software, intrusion detection systems (IDSs), intrusion protection systems (IPSs), constrained interfaces, as well as access control lists (ACLs) and encryption measures."

PHYSICAL = "This includes things like fences, gates, guards, security badges and access cards, biometric access controls, security lighting, CCTVs, surveillance cameras, motion sensors, fire suppression, as well as environmental controls like HVAC and humidity controls"

ADMIN = "employee hiring and termination, equipment and Internet usage, physical access to facilities, separation of duties, data classification, and auditing. Security awareness training for employees also falls under the umbrella of administrative controls."

print(f'LOGICAL:{dot_point(LOGIC)}\nPHYSICAL:{dot_point(PHYSICAL)}\nADMIN{dot_point(ADMIN)}')