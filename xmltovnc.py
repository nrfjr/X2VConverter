import sys
from xml.dom import minidom

def generate_vnc_files(file, save_dir):

    XMLfile = minidom.parse(file)

    for i in XMLfile.getElementsByTagName("file"):

        content = []
        save_file = open(f'{(save_dir)}{"/" if save_dir[-1]!="/" else ""}{i.getAttribute("name")}.vnc')

        content.append(f'ConnMethod=tcp\n')
        content.append(f'FriendlyName={i.getAttribute("name")}\n')
        content.append(f'Host={i.getAttribute("name")}\n')

        for j in i.getElementsByTagName("section"):

            for k in j.getElementsByTagName("param"):

                if k.getAttribute("name") is "Identity":
                    content.append(f'Identity={k.getAttribute("value")}\n')
                elif k.getAttribute("name") is "Password":
                    content.append(f'Password={k.getAttribute("value")}\n')
        
        content.pop()

def main():

    if len(sys.argv) > 3:
        printf(f'Too many arguments')
    elif len(sys.argv) == 2 or 0:
        print(f'Too few argument.')
    else:
        file = sys.argv[1] if sys.argv[1]  else input("Enter RealVNC's xml file: ")
        save_dir = sys.argv[2] if sys.argv[2] input("Enter saving directory: ")

    generate_vnc_files(file, save_dir)

main()
    
 


