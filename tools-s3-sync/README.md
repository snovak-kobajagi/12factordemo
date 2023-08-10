# 12 Factor CLI app

App prikazuje težnju ka idealnom software development workflow-u, primeni dobrih principa software craftsmanshipa, kao i 12 factor principa https://12factor.net/

## Libs na projektu

- Typer za apstrakciju rada sa CLI, sva biznis logika se piše u zasebnim komandama, izolovana
- Boto3 za apstrakciju rada sa AWS servisima
- Config se oslanja na env u non-prod okruženju, za prod okruženje čita uz pomoć boto3 iz Secrets managera

## Testiranje

- Pytest uz Moto, omogucava mockovanje AWS servisa, kako bi mogli pisati izolovane testove

## Run from Docker

- Moguce je koristiti CLI preko Dockera u interactive mode-u posle build-a: docker run -it tools-s3-sync
