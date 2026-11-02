# Cómo colaborar

Este repositorio contiene la presentación pública de Roger F5. Para cambios en una herramienta, utiliza el repositorio de esa herramienta.

## Proponer una mejora

Abre un issue con el problema observado, el enlace afectado y el resultado esperado. Los errores de presentación, enlaces y documentación pueden comunicarse públicamente. Para vulnerabilidades, utiliza el canal privado indicado en [SECURITY.md](SECURITY.md).

## Preparar un pull request

1. Crea una rama para una mejora concreta.
2. Conserva el logo original y comprueba que los datos profesionales y enlaces correspondan a fuentes públicas.
3. Guarda los recursos visuales en `assets/` y añade texto alternativo descriptivo.
4. Ejecuta la validación desde la raíz del repositorio:

   ```sh
   python .github/scripts/check_profile.py
   git diff --check
   ```

5. Describe qué cambia, enlaza el issue correspondiente y detalla la comprobación realizada.

La comprobación automática valida referencias locales y archivos SVG. Revisa también la presentación del README en GitHub antes de fusionar cambios visuales.

No incluyas credenciales, datos personales de terceros, certificados internos ni documentos de empresas o clientes. Atribuye las contribuciones a quienes hayan participado realmente.
