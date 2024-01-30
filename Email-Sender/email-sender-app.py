import os, smtplib, threading
from colorama import Fore
from tkinter import *
from tkinter import filedialog
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# ----------------- Main Screen -----------------
app = Tk()
app.geometry("610x410")
app.title("E-Mail Sender | Rohith")

# ----------------- Font Details -----------------
font_style = ('Times', 12)
font_bold_style = ('Times', 12, 'bold')
heading_style = ('Cambria', 15, 'bold')

# ----------------- Functions -----------------
def send():
    def send_email():
        try:
            msg = MIMEMultipart()
            sender = uname.get()
            app_password = password.get()
            receivers = receiver.get().split(',')
            subject_details = subject.get()
            body_message = body_entry.get("1.0", END)

            msg['From'] = sender
            msg['To'] = ', '.join(receivers)
            msg['Subject'] = subject_details

            # Attach text message
            msg.attach(MIMEText(body_message, 'plain'))

            if attachments_lst:
                for attachment in attachments_lst:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(open(attachment, 'rb').read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment)}')
                    msg.attach(part)

            if sender == "" or app_password == "" or not receivers or subject_details == "" or body_message == "":
                status.config(text="All Fields Required 😞", fg="red")
            else:
                print("Please Wait! Connecting To The Server...")
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender, app_password)
                
                for receiver_mail in receivers:
                    try:
                        server.sendmail(sender, receiver_mail.strip(), msg.as_string())
                        print(Fore.GREEN + f"Mail Sent Successfully to {receiver_mail.strip()} ✔" + Fore.RESET)
                    except:
                        print(Fore.RED + f"Failed to send email to {receiver_mail.strip()}." + Fore.RESET)
                server.quit()

                status.config(text="Email(s) has been sent 👍", fg="green")
        except smtplib.SMTPAuthenticationError:
            status.config(text="Error! Invalid Credentials 😓", fg="red")
            print(Fore.RED + "Failure in Sending Email! Enter Valid Details." + Fore.RESET)
            print(f"Details of Error: {Fore.YELLOW}Username and Password not accepted{Fore.RESET}")

    threading.Thread(target=send_email).start()

def attach_file():
    default_folder = os.path.expanduser('~/Downloads')
    filenames = filedialog.askopenfilenames(initialdir=default_folder, title='Select the File')
    if filenames:
        attachments_lst.extend(filenames)
        status.config(fg='green', text='Attached ' + str(len(attachments_lst)) + ' File(s)')

def reset():
    attachments_lst.clear()
    uname.set("")
    password.set("")
    receiver.set("")
    subject.set("")
    body_entry.delete("1.0", END)
    status.config(text="")

    print(Fore.LIGHTCYAN_EX + "All Fields are Cleared 👍" + Fore.RESET)

# ----------------- Heading -----------------
label = Label(app, text="Email App - Rohith", font=heading_style, fg='blue')
label.grid(row=0, column=1, sticky=W, padx=30, pady=(0, 10), columnspan=2)

# ----------------- Additional Text -----------------
Label(app, text="To email multiple recipients, separate their addresses with commas(,) in the 'To' text field.", font=font_style, fg='gray').grid(row=1, column=0, padx=20, pady=(0, 15), columnspan=10)

# ----------------- Field Labels -----------------
Label(app, text="Email", font=font_bold_style).grid(row=2, sticky=W, padx=50, pady=2)
Label(app, text="Password", font=font_bold_style).grid(row=3, sticky=W, padx=50, pady=2)
Label(app, text="To", font=font_bold_style).grid(row=4, sticky=W, padx=50, pady=2)
Label(app, text="Subject", font=font_bold_style).grid(row=5, sticky=W, padx=50, pady=2)
Label(app, text="Body", font=font_bold_style).grid(row=6, sticky=W, padx=50, pady=2)

status = Label(app, text="", font=font_style)
status.grid(row=9, sticky=S, padx=10, columnspan=2)

# ----------------- Storage Variables -----------------
uname = StringVar()
password = StringVar()
receiver = StringVar()
subject = StringVar()
attachments_lst = []

# ----------------- Entries -----------------
uname_entry = Entry(app, textvariable=uname, font=font_style, width=25)
uname_entry.grid(row=2, column=1, pady=2)

password_entry = Entry(app, textvariable=password, show='•', font=font_style, width=25)
password_entry.grid(row=3, column=1, pady=2)

receiver_entry = Entry(app, textvariable=receiver, font=font_style, width=25)
receiver_entry.grid(row=4, column=1, pady=2)

subject_entry = Entry(app, textvariable=subject, font=font_style, width=25)
subject_entry.grid(row=5, column=1, pady=2)

body_entry = Text(app, font=font_style, height=5, width=40)
body_entry.grid(row=6, column=1, pady=2)

# ----------------- Button Fields -----------------
Button(app, text="Send", font=font_bold_style, bg='green', fg='white', width=10, command=send).grid(row=7, sticky=W, padx=50, pady=20)
Button(app, text="Reset", font=font_bold_style, bg='#8458B3', fg='white', width=10, command=reset).grid(row=7, column=1, sticky=W, pady=20)
Button(app, text="Attach File", font=font_bold_style, bg='violet', command=attach_file).grid(row=7, column=1, sticky=E, padx=5)

app.mainloop()
