# python_intrusion

Collection de scripts Python développés lors du mode Sécurité offensive.

## Organisation

* correction : contient l'ensemble des scripts de Glenn donnés lors de la correction.

Merci de faire un dossier à votre nom et y mettre vos scripts à l'intérieur pour garder l'ensemble organisé.

## Compilation d'un script

```
pip install pyinstaller
# -F : produit un seul fichier
# -w : cache la fenêtre python
# -i : icône du binaire produit
pyinstaller -F -w -i icone.ico script.py
```