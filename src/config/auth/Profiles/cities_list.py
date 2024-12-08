from django.db import models


# A list of states and cities in Germany, for example.

class StateChoices(models.TextChoices):
    BADEN_WUERTTEMBERG = 'Baden-Württemberg'
    BAVARIA = 'Bavaria'
    BERLIN = 'Berlin'
    BRANDENBURG = 'Brandenburg'
    BREMEN = 'Bremen'
    HAMBURG = 'Hamburg'
    HESSE = 'Hesse'
    LOWER_SAXONY = 'Lower Saxony'
    MECKLENBURG_WESTERN_POMERANIA = 'Mecklenburg-Western Pomerania'
    NORTH_RHINE_WESTPHALIA = 'North Rhine-Westphalia'
    RHINELAND_PALATINATE = 'Rhineland-Palatinate'
    SAARLAND = 'Saarland'
    SAXONY = 'Saxony'
    SAXONY_ANHALT = 'Saxony-Anhalt'
    SCHLESWIG_HOLSTEIN = 'Schleswig-Holstein'
    THURINGIA = 'Thuringia'


class CitiesChoices(models.TextChoices):
    # Baden-Württemberg
    STUTTGART = 'Stuttgart (Baden-Württemberg)'
    KARLSRUHE = 'Karlsruhe (Baden-Württemberg)'
    MANNHEIM = 'Mannheim (Baden-Württemberg)'

    # Bavaria
    MUNICH = 'Munich (Bavaria)'
    NUREMBERG = 'Nuremberg (Bavaria)'
    AUGSBURG = 'Augsburg (Bavaria)'

    # Berlin
    BERLIN = 'Berlin (Berlin)'

    # Brandenburg
    POTSDAM = 'Potsdam (Brandenburg)'
    COTTBUS = 'Cottbus (Brandenburg)'

    # Bremen
    BREMEN = 'Bremen (Bremen)'

    # Hamburg
    HAMBURG = 'Hamburg (Hamburg)'

    # Hesse
    FRANKFURT = 'Frankfurt (Hesse)'
    WIESBADEN = 'Wiesbaden (Hesse)'
    DARMSTADT = 'Darmstadt (Hesse)'

    # Lower Saxony
    HANNOVER = 'Hannover (Lower Saxony)'
    BRAUNSCHWEIG = 'Braunschweig (Lower Saxony)'

    # Mecklenburg-Western Pomerania
    ROSTOCK = 'Rostock (Mecklenburg-Western Pomerania)'
    SCHWERIN = 'Schwerin (Mecklenburg-Western Pomerania)'

    # North Rhine-Westphalia
    COLOGNE = 'Cologne (North Rhine-Westphalia)'
    DUSSELDORF = 'Düsseldorf (North Rhine-Westphalia)'
    DORTMUND = 'Dortmund (North Rhine-Westphalia)'

    # Rhineland-Palatinate
    MAINZ = 'Mainz (Rhineland-Palatinate)'
    LUDWIGSHAFEN = 'Ludwigshafen (Rhineland-Palatinate)'

    # Saarland
    SAARBRUCKEN = 'Saarbrücken (Saarland)'

    # Saxony
    DRESDEN = 'Dresden (Saxony)'
    LEIPZIG = 'Leipzig (Saxony)'

    # Saxony-Anhalt
    MAGDEBURG = 'Magdeburg (Saxony-Anhalt)'
    HALLE = 'Halle (Saxony-Anhalt)'

    # Schleswig-Holstein
    KIEL = 'Kiel (Schleswig-Holstein)'
    LUEBECK = 'Lübeck (Schleswig-Holstein)'

    # Thuringia
    ERFURT = 'Erfurt (Thuringia)'
    JENA = 'Jena (Thuringia)'
