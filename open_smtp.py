import multiprocessing as mp
import smtplib

counter = mp.Value('i', 0)
def testServer(host, port=465):
	global counter
	with counter.get_lock():
		counter.value += 1
	if counter.value%10 == 0:
		print(f'{counter.value}')
	try:
		s = smtplib.SMTP(host=host, port=port, timeout=5)
		s.sendmail('wtf@lmao.com', [f"admin@{'.'.join(host.split('.')[1:])}"], 'dude lmao wtf xddd')
		print(f'\n{host}\n')
		return host
	except Exception as e:
		print(e)
		return False

if __name__== '__main__':
	with open('mxfinal.txt') as f:
		hosts = f.readlines()
	print('+')
	hosts = [host.rstrip() for host in hosts]
	p = mp.Pool(16)
	res = p.map(testServer, hosts)
	with open('results.txt', 'w') as f:
		for host in res:
			if host:
				f.write(f'{host}\n')
