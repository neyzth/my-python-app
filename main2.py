class Vehicule:
    """Classe de base représentant un véhicule."""
    def __init__(self, marque: str, modele: str, vitesse: int = 0, vmax: int = 200, freinage: str = "hydraulique") -> None:
        self.marque = marque
        self.modele = modele
        self.vitesse = vitesse
        self.vmax = vmax
        self.freinage = freinage

    def description(self):
        return f"{self.marque} {self.modele}, vitesse : {self.vitesse} km/h, Vmax : {self.vmax} km/h, freinage : {self.freinage}"

    def accelerer(self, vitesse: int):
        self.vitesse = min(self.vmax, self.vitesse + vitesse)
        return f"Le véhicule accélère de {vitesse} km/h, vitesse actuelle : {self.vitesse} km/h"

    def freiner(self):
        self.vitesse = max(0, self.vitesse - 10)
        return f"Le véhicule freine, vitesse actuelle : {self.vitesse} km/h"


class Thermique(Vehicule):
    """Classe représentant un véhicule thermique."""
    def __init__(self, marque: str, modele: str, carburant: str = "Essence", vitesse: int = 0, vmax: int = 200, freinage: str = "hydraulique") -> None:
        super().__init__(marque, modele, vitesse, vmax, freinage)
        self.carburant = carburant

    def description(self):
        return f"{super().description()} - Type : Thermique ({self.carburant})"


class Electrique(Vehicule):
    """Classe représentant un véhicule électrique."""
    def __init__(self, marque: str, modele: str, autonomie: int, vitesse: int = 0, vmax: int = 200, freinage: str = "régénératif") -> None:
        super().__init__(marque, modele, vitesse, vmax, freinage)
        self.autonomie = autonomie

    def description(self):
        return f"{super().description()} - Type : Électrique ({self.autonomie} km d'autonomie)"


class Voiture(Thermique):
    """Classe représentant une voiture thermique."""
    def __init__(self, marque: str, modele: str, carburant: str = "Essence", vitesse: int = 0, vmax: int = 220, portes: int = 5, freinage: str = "hydraulique") -> None:
        super().__init__(marque, modele, carburant, vitesse, vmax, freinage)
        self.portes = portes

    def description(self):
        return f"{super().description()} - Nombre de portes : {self.portes}"


class VoitureElectrique(Electrique):
    """Classe représentant une voiture électrique."""
    def __init__(self, marque: str, modele: str, autonomie: int, vitesse: int = 0, vmax: int = 250, portes: int = 5, freinage: str = "régénératif") -> None:
        super().__init__(marque, modele, autonomie, vitesse, vmax, freinage)
        self.portes = portes

    def description(self):
        return f"{super().description()} - Nombre de portes : {self.portes}"


class Scooter(Thermique):
    """Classe représentant un scooter thermique."""
    def __init__(self, marque: str, modele: str, carburant: str = "Essence", vitesse: int = 0, vmax: int = 120, freinage: str = "hydraulique") -> None:
        super().__init__(marque, modele, carburant, vitesse, vmax, freinage)


class ScooterElectrique(Electrique):
    """Classe représentant un scooter électrique."""
    def __init__(self, marque: str, modele: str, autonomie: int, vitesse: int = 0, vmax: int = 100, freinage: str = "régénératif") -> None:
        super().__init__(marque, modele, autonomie, vitesse, vmax, freinage)


if __name__ == "__main__":
    voiture_t = Voiture("Peugeot", "208", "Diesel", portes=5)
    voiture_e = VoitureElectrique("Tesla", "Model 3", autonomie=450, portes=4)
    scooter_t = Scooter("Yamaha", "Xmax", "Essence")
    scooter_e = ScooterElectrique("Niu", "NQi", autonomie=100)

    print(voiture_t.description())
    print(voiture_e.description())
    print(scooter_t.description())
    print(scooter_e.description())

    print(voiture_t.accelerer(20))
    print(scooter_e.accelerer(15))
    print(voiture_t.freiner())
    print(scooter_e.freiner())
