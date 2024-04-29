def send_message(ssh_client, message):
    ssh_client.exec_command(f"echo '{message}' > /tmp/message.txt")
    ssh_client.exec_command("cat /tmp/message.txt")
