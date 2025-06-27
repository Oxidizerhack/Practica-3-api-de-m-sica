from django.db import models

# Create your models here.

class Instrumentos(models.Model):
    TIPOS_INSTRUMENTOS = [
    ("CUERDA_ANDINA", "Cuerda andina"),        # Charango, ronroco, guitarrilla
    ("VIENTO_ANDINO", "Viento andino"),        # Quena, zampoña, tarka, moseño
    ("PERCUSION_FOLKLORICA", "Percusión folklórica"),  # Bombo, caja, tambor, matraca
    ("TECLADO_POPULAR", "Teclado popular"),    # Órganos o teclados modernos en grupos
    ("ELECTRONICO_FUSION", "Electrónico fusión"), # Sintetizadores en grupos fusión folklórica
    ("AUTOCTONO", "Autóctono ceremonial"),     # Pututu, cuerno, instrumentos rituales
]
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=TIPOS_INSTRUMENTOS)

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"
    
    
class Ritmo(models.Model):
    RITMOS_BOLIVIANOS = [
    ("MORENADA", "Morenada"),
    ("CAPORAL", "Caporal"),
    ("DIABLADA", "Diablada"),
    ("TINKU", "Tinku"),
    ("KULLAWADA", "Kullawada"),
    ("WACA_WACA", "Waca Waca"),
    ("SAYA", "Saya"),
    ("HUAYNO", "Huayño"),
    ("PUJLLAY", "Pujllay"),
    ("SICURI", "Sicuri"),
    ("TONADA", "Tonada"),
    ("CUECA", "Cueca"),
    ("CUECA_CHAPACA", "Cueca chapaca"),
    ("BAILECITO", "Bailecito"),
    ("TAQUIRARI", "Taquirari"),
    ("CARNAVALITO", "Carnavalito"),
    ("CHOVENA", "Chovena"),
    ("MACHETEROS", "Macheteros"),
    ("TUNDIQUI", "Tundiqui"),
    ("MUSICA_MOJENA", "Música mojeña"),
]
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    instrumentos = models.ManyToManyField(Instrumentos, related_name="ritmos")
    def __str__(self):
        return self.nombre

    

class Departamento(models.Model):
    UBICACION_BOLIVIANAS = [
        ('Sur', 'Sur'),
        ('Occidente', 'Occidente'),
        ('Oriente', 'Oriente'),
        ('Centro', 'Centro'),
        ('Norte', 'Norte'),
    ]

    nombre = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=20, choices=UBICACION_BOLIVIANAS)

    def __str__(self):
        return f"{self.nombre} ({self.ubicacion})"
    

class Agrupacion(models.Model):
    TIPO_AGRUPACION = [
        ('SOLISTA', 'Solista'),
        ('GRUPAL', 'Grupal'),
        ('DUO', 'Dúo'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(
        help_text="Descripción breve del grupo o artista"
    )
    tipo = models.CharField(
        max_length=10,
        choices=TIPO_AGRUPACION,
        default='GRUPAL',
        help_text="Tipo de agrupación: solista, grupal o dúo"
    )

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"


class Cancion(models.Model):
    TITULO_CANCIONES = [
    # Los Kjarkas
    ("LK", "Llorando se fue"),
    ("LK", "Wayayay"),
    ("LK", "Cholitas lindas"),

    # Savia Andina
    ("SA", "Tunkata P'a La Cumbre"),
    ("SA", "Potosina"),
    ("SA", "Lamento Indio"),

    # Grupo Raíces
    ("GR", "El Indio"),
    ("GR", "Chola paceña"),
    ("GR", "Oruro es leyenda"),

    # Inkuyo
    ("IN", "Cruzando el Altiplano"),
    ("IN", "Oruro"),
    ("IN", "La Partida"),

    # Grupo Llajtaymanta
    ("GL", "Tinku"),
    ("GL", "Morenada"),
    ("GL", "Saya"),

    # Kala Marka
    ("KM", "Carnaval de Oruro"),
    ("KM", "Danza de los Tobas"),
    ("KM", "Fiesta Andina"),

    # Wara
    ("WR", "Pachamama"),
    ("WR", "Flor de los Andes"),
    ("WR", "Viento Andino"),

    # Flor de Piedra
    ("FP", "Canto a la Madre"),
    ("FP", "Danza de la Llama"),
    ("FP", "Sueños Andinos"),

    # Bolivia Mía
    ("BM", "Bolivia Mía"),
    ("BM", "Leyenda del Altiplano"),
    ("BM", "Ojos de mi Tierra"),

    # Antología
    ("AN", "Danza del Inca"),
    ("AN", "Nostalgia Andina"),
    ("AN", "Recuerdos de mi Pueblo"),

    # Tinku
    ("TK", "Ritmo del Tinku"),
    ("TK", "Danza de Guerreros"),
    ("TK", "Fiesta Andina"),

    # Sangre Boliviana
    ("SB", "Sangre de mi Tierra"),
    ("SB", "Huayño Profundo"),
    ("SB", "Eco Andino"),

    # Awatiñas
    ("AW", "Flor de la Noche"),
    ("AW", "Vientos del Altiplano"),
    ("AW", "Melodías del Ande"),

    # Pacha
    ("PC", "Pachamama Sagrada"),
    ("PC", "Tierra y Cielo"),
    ("PC", "Ritual Andino"),

    # Sangre Andina
    ("SA2", "Andes Eternos"),
    ("SA2", "Canto a la Vida"),
    ("SA2", "Luz del Sol"),

    # Alborada
    ("AL", "Alborada Andina"),
    ("AL", "Danza del Sol"),
    ("AL", "Ritmo y Tradición"),

    # Grupo Saya
    ("GS", "Saya Negra"),
    ("GS", "Carnaval Afro"),
    ("GS", "Raíces de mi Pueblo"),

    # Tukuy Runa
    ("TR", "Pueblo Unido"),
    ("TR", "Corazón Andino"),
    ("TR", "Voces de la Tierra"),

    # Condor y Cóndor
    ("CC", "Vuelo del Cóndor"),
    ("CC", "Alas de Libertad"),
    ("CC", "Montañas y Cielos"),

    # K'ala Marka
    ("KM2", "Danza del Carnaval"),
    ("KM2", "Ritmos Ancestrales"),
    ("KM2", "Fiesta de los Andes"),

    # Llamerada
    ("LL", "Danza de Llamas"),
    ("LL", "Pasos de mi Pueblo"),
    ("LL", "Ritual Andino"),

    # Tunari
    ("TU", "Ecos del Tunari"),
    ("TU", "Montaña y Viento"),
    ("TU", "Cantos del Valle"),

    # Los Chaskis
    ("LC", "Mensajeros del Ande"),
    ("LC", "Viento y Fuego"),
    ("LC", "Ritmo Tradicional"),

    # Chila Jatun
    ("CJ", "Sombras Andinas"),
    ("CJ", "Canto Profundo"),
    ("CJ", "Tierra Viva"),

    # Los Diplomáticos
    ("LD", "Danza Popular"),
    ("LD", "Fiesta en el Altiplano"),
    ("LD", "Ritmos y Tradiciones"),

    # Grupo Pachamama
    ("GP", "Canto a la Pachamama"),
    ("GP", "Danza Sagrada"),
    ("GP", "Ritmo de la Tierra"),

    # Kunan Runa
    ("KR", "Triste Amor"),
    ("KR", "Kachatikitay"),
    ("KR", "Agonias"),
    ] 
  
    nombre = models.CharField(max_length=100)
    agrupacion = models.ForeignKey(Agrupacion, on_delete=models.CASCADE)
    instrumentos = models.ManyToManyField(Instrumentos, blank=True)
    ritmos = models.ManyToManyField(Ritmo, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.agrupacion.nombre}"



