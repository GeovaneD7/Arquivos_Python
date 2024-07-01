"""Script criado apenas para aprender interpolação clássica."""
__version__ = "0.0.1"
__author__ = "Geovane Dias"

email_tmpl = """
    Olá, %(nome)s,
    Você foi convidado a participar da %(feiraid)d de RPG.
    Para participar basta entrar no link: %(link)s.
    Corra que restam apenas %(vagas)d restantes.
    O valor da inscrição é de apenas %(valor).2f por tempo limitado!
    Estamos esperando você!"""
   
convidados = ["Geovane", "Marina", "Ketlen"]
   
for i in convidados:
        print(
            email_tmpl
            % {
                "nome": i,
                "feiraid": 5,
                "link": "https://conviteRPG.com",
                "vagas": 2,
                "valor": 5000.00
            }
        )