import speedtest

test = speedtest.Speedtest()

test.get_servers()
best = test.get_best_server()

print(f"Found: {best['host']} located in {best['country']}")

print("Download Speed...")
down = test.download()
print(f"Download Speed: {down / 1024 /1024 :.2f} Mb/s")

print("Upload Speed...")
up = test.upload()
print(f"Upload Speed: {up / 1024 /1024 :.2f} Mb/s")

ping = test.results.ping
print(f"Ping: {ping} ms")