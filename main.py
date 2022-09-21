import server


if __name__ == '__main__':
    host = server.HostServer()

    try:
        print('Server ON')
        host.\
            starhost().\
            serve_forever()  # -> server.py -> HostServer -> run server -> nasłuchiwanie

    except KeyboardInterrupt:
        print('Server OFF')
        host.stophost()

    



# Bazaa danych User (imie nazwisko)
# sd
#html z css 
#javascript z wysyłaniem json 
#<-:

"""
git
    init
    add <file name> / . / -all
    commit -m "adfgadfghgfeggghgfhgfg"
    branch paweł
    git push -u origin paweł

"""