# Localyze — site

Site estático (HTML + CSS + JS, sem build) de foto e vídeo, Canoas e região.

## Publicar no Cloudflare Pages (grátis)

1. Crie uma conta em https://dash.cloudflare.com e abra **Workers & Pages → Create → Pages → Connect to Git**.
2. Escolha este repositório (`Codingal-Classes`) e a branch que contém a pasta `localyze`.
3. Configurações do projeto:
   - **Project name:** o nome que vira o endereço (`nome.pages.dev`)
   - **Build command:** deixe vazio
   - **Build output directory:** `localyze`
4. Salve e aguarde. O site abre em `https://nome.pages.dev`.

Depois de saber o endereço final, troque `https://localyze.pages.dev/img/og.jpg` no `index.html`
(tag `og:image`) pelo endereço real, para a prévia do link aparecer certa no WhatsApp.

## Onde mudar as coisas

| O quê | Onde |
|---|---|
| Textos, telefone, e-mail, Instagram | `index.html` |
| Cores (azul claro, claro/escuro) | `style.css`, bloco `:root` no começo |
| Fotos | pasta `img/` (use `.webp`) |
| Seção "Trabalhos" (desligada) | `index.html`, `<section id="trabalhos" hidden>`: apague `hidden` e adicione as fotos |

WhatsApp: o link `wa.me/5551989006644` já abre com a mensagem pronta
("Olá, Andrade! Vi a apresentação da Localyze e quero um orçamento.").

## Fontes
Barlow e Barlow Condensed (licença SIL OFL), hospedadas na própria pasta `fonts/`.
