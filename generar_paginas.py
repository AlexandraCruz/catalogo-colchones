import csv
import os

CSV_FILE = 'meta-feed.csv'
OUTPUT_FOLDER = 'productos'

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="es-DO">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Colchonería Godfrey</title>
<meta name="description" content="{description}">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@600;700&family=Public+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@500&display=swap" rel="stylesheet">
<style>
  :root{{
    --cotton:#EFEAE0; --ink:#23262B; --ink-soft:#54524B;
    --indigo:#2B3A55; --brick:#A6472B; --line:#D3C9B4; --card:#FBF9F4;
  }}
  body{{ margin:0; background:var(--cotton); color:var(--ink); font-family:'Public Sans',sans-serif; }}
  header{{ padding:16px 24px; border-bottom:1px solid var(--line); display:flex; justify-content:space-between; align-items:center; background:#fff; }}
  .back-btn{{ font-family:'IBM Plex Mono',monospace; font-size:.7rem; text-decoration:none; color:var(--ink-soft); text-transform:uppercase; }}
  
  main{{ max-width:1000px; margin:40px auto; padding:24px; display:grid; grid-template-columns: 1fr 1fr; gap:40px; }}
  
  /* CONTENEDOR DE IMAGEN 1:1 */
  .product-image-container {{
    width: 100%;
    aspect-ratio: 1 / 1; /* Esto garantiza que sea un cuadrado perfecto */
    background: var(--cotton-2); /* Color de fondo mientras no hay imagen */
    border: 1px solid var(--line);
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
  }}
  .product-image-container img {{
    width: 100%;
    height: 100%;
    object-fit: cover; /* La imagen llenará el cuadrado sin deformarse */
  }}
  .placeholder-text {{ color: var(--line); font-family: 'IBM Plex Mono', monospace; font-size: 0.8rem; }}

  .details {{ padding: 20px 0; }}
  .eyebrow {{ font-family:'IBM Plex Mono',monospace; font-size:.7rem; color:var(--brick); text-transform:uppercase; margin-bottom:10px; display:block; }}
  h1 {{ font-family:'Fraunces',serif; font-size:2.5rem; margin:0 0 15px; line-height:1.1; }}
  .price {{ font-family:'IBM Plex Mono',monospace; font-size:2rem; color:var(--indigo); margin-bottom:20px; }}
  .description {{ line-height:1.6; color:var(--ink-soft); margin-bottom:30px; font-size:1.1rem; }}
  
  .cta-wa {{
    display:inline-block; background:var(--brick); color:#fff; text-decoration:none;
    padding:16px 32px; font-family:'IBM Plex Mono',monospace; text-transform:uppercase; font-weight:600;
  }}

  @media (max-width: 768px) {{
    main {{ grid-template-columns: 1fr; }}
  }}
</style>
</head>
<body>
<header>
  <a href="../index.html" style="font-family:'Fraunces',serif; font-weight:700; text-decoration:none; color:inherit;">Godfrey</a>
  <a href="../index.html" class="back-btn">← Volver al catálogo</a>
</header>

<main>
  <div class="product-image-container">
    <!-- Aquí colocarás tu imagen después. El espacio ya es 1:1 cuadrado -->
    <!-- El navegador sale de /productos y entra a /images -->
    <img src="../images/{id}.jpg" alt="{title}" onerror="this.style.display='none';">
    <div class="placeholder-text" style="position:absolute; z-index:-1;">Cargando imagen... IMAGEN 1:1 ESPACIO RESERVADO</div>
  </div>

  <div class="details">
    <span class="eyebrow">{brand}</span>
    <h1>{title}</h1>
    <div class="price">RD$ {price}</div>
    <p class="description">{description}</p>
    <a href="https://wa.me/18297664304?text=Hola, quiero información sobre: {title}" class="cta-wa" target="_blank">Consultar por WhatsApp</a>
  </div>
</main>
</body>
</html>
"""

def generate():
    with open(CSV_FILE, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            filename = row['link'].split('/')[-1]
            price_clean = row['price'].replace(' DOP', '')
            
            html_content = HTML_TEMPLATE.format(
                title=row['title'],
                description=row['description'],
                price=price_clean,
                brand=row['brand'],
                id=row['id']
            )

            with open(os.path.join(OUTPUT_FOLDER, filename), 'w', encoding='utf-8') as out:
                out.write(html_content)
            print(f"Creado: {filename}")

if __name__ == "__main__":
    generate()