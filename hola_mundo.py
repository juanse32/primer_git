import siaskynet as skynet

# create a client
client = skynet.SkynetClient()

# upload
skylink = client.upload_file("./src.jpg")
print("Upload successful, skylink: " + skylink)

# download
client.download_file("./dst.jpg", skylink)
print("Download successful")