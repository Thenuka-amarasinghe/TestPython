import os
from tkinter import *

root = Tk()
root.geometry("1000x600+150+25")
root.title("MainMenu")
root.resizable(width=False, height=False)
root.columnconfigure(1, weight=1)
root.rowconfigure(8)

Home = Frame(root, bg='blue', height='600', width='800')
Reports = Frame(root, bg='yellow', height='600', width='800')
Search = Frame(root, bg='red', height='600', width='800')
Metadata = Frame(root, bg='green', height='600', width='800')
WriteBlocker = Frame(root, bg='cyan', height='600', width='800')
LogFile = Frame(root, bg='purple', height='600', width='800')
Decrypt = Frame(root, bg='violet', height='600', width='800')
Send = Frame(root, bg='grey', height='600', width='800')

# Home Frame
Home.grid(row='0', column='1', rowspan='8')


# Reports

def run_ipconfig():
    txtbox.configure(state=NORMAL)
    response = os.popen('ipconfig /all')
    txtbox.insert(END, "\n\nAll network configurations:\n\n")
    for x in response:
        txtbox.insert(END, x)
    txtbox.configure(state=DISABLED)


def fin():
    NetStatReport = open('NetworkStatsReport.txt', 'w')
    response = txtbox.get("1.0", END)
    for x in response:
        NetStatReport.write(x)
    return


def run_ping():
    txtbox.configure(state=NORMAL)
    ping_site = ping_text.get()
    response = os.popen('ping ' + ping_site)
    txtbox.insert(END, "\n\nPing Results of : " + ping_site + "\n\n")
    for x in response:
        txtbox.insert(END, x)
    txtbox.configure(state=DISABLED)

def run_nic():
    txtbox.configure(state=NORMAL)
    nicoptions = []
    nicoptions = [speed.get(), pysad.get()]
    ping_site = ping_text.get()
    response = os.popen("wmic NIC get Description,MACAddress" + nicoptions[0] + nicoptions[1])
    txtbox.insert(END, "\n\nNIC Information : \n\n")
    for x in response:
        txtbox.insert(END, x)
    txtbox.configure(state=DISABLED)


    #wmic NIC get Description, MACAddress, NetEnabled, Speed



scrollme = Scrollbar(Reports, orient=VERTICAL)
txtbox = Text(Reports, height=15, width=90, yscrollcommand=scrollme.set)
scrollme.configure(command=txtbox.yview)
txtbox.insert(1.0, "Network Configurations")
txtbox.configure(state=DISABLED)
fin_btn = Button(Reports, text='FINALIZE', command=fin)
ipconfig_btn = Button(Reports, text='ipconfig /all', command=run_ipconfig)
ping_btn = Button(Reports, text='Ping', command=run_ping)
ping_text = Entry(Reports)
nic_btn = Button(Reports, text='NIC', command=run_nic)

speed = StringVar()
pysad = StringVar()
nic_speed = Checkbutton(Reports, text="Speed", variable=speed, onvalue=', Speed', offvalue=' ')
nic_physicaladapter = Checkbutton(Reports, text="Physical Adapter", variable=pysad, onvalue=', PhysicalAdapter', offvalue=' ')
nic_speed.deselect()
nic_physicaladapter.deselect()

scrollme.grid(row=5, column=5, sticky='ns', pady=50)
txtbox.grid(row=5, column=1, columnspan=3, padx=(30, 0), pady=50)
fin_btn.grid(row=6, column=3)
ping_text.grid(row=2, column=2)
ping_btn.grid(row=2, column=1, sticky='ew', padx=10, pady=10)
ipconfig_btn.grid(row=1, column=1, sticky='ew', padx=10, pady=10)
nic_btn.grid(row=3, column=1, sticky='ew', padx=10, pady=10)
nic_speed.grid(row=3, column=2)
nic_physicaladapter.grid(row=3, column=3)


def gohome():
    Home.grid(row='0', column='1', rowspan='8', sticky='nesw')
    Reports.grid_forget()
    Search.grid_forget()
    Metadata.grid_forget()
    WriteBlocker.grid_forget()
    LogFile.grid_forget()
    Decrypt.grid_forget()
    Send.grid_forget()


def goreport():
    Home.grid_forget()
    Reports.grid(row='0', column='1', rowspan='8', sticky='nesw')
    Search.grid_forget()
    Metadata.grid_forget()
    WriteBlocker.grid_forget()
    LogFile.grid_forget()
    Decrypt.grid_forget()
    Send.grid_forget()


def gosearch():
    Home.grid_forget()
    Reports.grid_forget()
    Search.grid(row='0', column='1', rowspan='8', sticky='nesw')
    Metadata.grid_forget()
    WriteBlocker.grid_forget()
    LogFile.grid_forget()
    Decrypt.grid_forget()
    Send.grid_forget()


def gometa():
    Home.grid_forget()
    Reports.grid_forget()
    Search.grid_forget()
    Metadata.grid(row='0', column='1', rowspan='8', sticky='nesw')
    WriteBlocker.grid_forget()
    LogFile.grid_forget()
    Decrypt.grid_forget()
    Send.grid_forget()


def gowriteblocker():
    Home.grid_forget()
    Reports.grid_forget()
    Search.grid_forget()
    Metadata.grid_forget()
    WriteBlocker.grid(row='0', column='1', rowspan='8', sticky='nesw')
    LogFile.grid_forget()
    Decrypt.grid_forget()
    Send.grid_forget()


def gologfile():
    Home.grid_forget()
    Reports.grid_forget()
    Search.grid_forget()
    Metadata.grid_forget()
    WriteBlocker.grid_forget()
    LogFile.grid(row='0', column='1', rowspan='8', sticky='nesw')
    Decrypt.grid_forget()
    Send.grid_forget()


def godecrypt():
    Home.grid_forget()
    Reports.grid_forget()
    Search.grid_forget()
    Metadata.grid_forget()
    WriteBlocker.grid_forget()
    LogFile.grid_forget()
    Decrypt.grid(row='0', column='1', rowspan='8', sticky='nesw')
    Send.grid_forget()


def gosend():
    Home.grid_forget()
    Reports.grid_forget()
    Search.grid_forget()
    Metadata.grid_forget()
    WriteBlocker.grid_forget()
    LogFile.grid_forget()
    Decrypt.forget()
    Send.grid(row='0', column='1', rowspan='8', sticky='nesw')


MenuBar = Frame(root, height='600', width='200').grid(row='0', column='0', rowspan='8')

home_btn = Button(MenuBar, text="HOME", command=gohome).grid(row='0', column='0', sticky='nesw')
reports_btn = Button(MenuBar, text="REPORTS", command=goreport).grid(row='1', column='0', sticky='nesw')
search_btn = Button(MenuBar, text="SEARCH", command=gosearch).grid(row='2', column='0', sticky='nesw')
meta_btn = Button(MenuBar, text="METADATA", command=gometa).grid(row='3', column='0', sticky='nesw')
writeblock_btn = Button(MenuBar, text="WRITE BLOCKER", command=gowriteblocker).grid(row='4', column='0', sticky='nesw')
logfile_btn = Button(MenuBar, text="LOG FILE", command=gologfile).grid(row='5', column='0', sticky='nesw')
decrypt_btn = Button(MenuBar, text="DECRYPT", command=godecrypt).grid(row='6', column='0', sticky='nesw')
send_btn = Button(MenuBar, text="SEND", command=gosend).grid(row='7', column='0', sticky='nesw')

root.mainloop()
