# Jogo Roblox: Simulador de Plantação com Drones

Anotações salvas da conversa de planejamento (setembro/2026), para retomar depois.

## Conceito

Simulador de fazenda no estilo *Grow a Garden* (gênero mais jogado do Roblox
hoje), com um diferencial: a automação da plantação/colheita é feita por
**drones** que o jogador compra e melhora, em vez de um bot externo/cheat.

## Loop principal

plantar → crescer → colher → vender → upgrade

## Drones (a mecânica central do jogo)

- **Drone Plantador** — planta sementes automaticamente nos espaços vazios
- **Drone Regador** — acelera o crescimento das plantas
- **Drone Colhedor** — recolhe o que está maduro e leva ao ponto de venda
- **Drone Vigia** — defende a fazenda contra pragas e (ver seção PvP) contra
  invasões de outros jogadores

Cada drone é upgradável: velocidade, capacidade, alcance, número de plantas
que consegue cuidar ao mesmo tempo.

## Sistemas extras (para enriquecer o jogo)

1. **Mutações raras** — chance pequena de uma planta nascer "dourada"/rara,
   valendo muito mais (mecânica de sorte, comprovadamente viciante nos
   simuladores de sucesso)
2. **Clima dinâmico** — chuva acelera crescimento; tempestade pode destruir
   a colheita se os drones não estiverem ativos
3. **Terrenos expansíveis** — comprar mais espaço de plantação com moedas
4. **Visitar fazenda de amigos** — gancho social
5. **Skins cosméticas de drones** — possível monetização opcional futura
   (nunca obrigatória para jogar)

## Camada social/PvP (inspirada em Steal a Brainrot)

Pesquisa mostrou que o fator #1 do sucesso do *Steal a Brainrot* (recorde
histórico: 25,8M jogadores simultâneos, mais que qualquer jogo já teve) foi
a mecânica social de **roubar/defender**, não o grind sozinho.

Ideia para o nosso jogo: outros jogadores podem invadir a fazenda e tentar
sequestrar um drone ou roubar parte da colheita; o jogador defende com o
**Drone Vigia**. É uma mecânica de jogo legítima (dentro do próprio game,
multiplayer), diferente de um bot/script externo para jogar sozinho — isso
nunca faz parte do escopo.

## O que fazer para tentar viralizar

Fatores identificados na pesquisa sobre jogos virais do Roblox:

- **Primeira sessão rápida e recompensadora** — primeiro drone em menos de
  2 minutos, sem tutorial arrastado
- **Momentos "clipáveis"** — efeito visual/sonoro exagerado quando um drone
  é roubado ou uma planta mutante rara aparece, para virar clipe de TikTok
  naturalmente
- **Estética com potencial de meme** — nomes/skins de drones engraçados e
  absurdos
- **Leaderboard social** — "maior fazenda", "mais drones roubados", etc.

Estratégia de divulgação (fora do jogo):
- TikTok é o principal motor de descoberta de jogos Roblox hoje (60%+ dos
  usuários ativos do TikTok também jogam Roblox)
- Parcerias com criadores de conteúdo (TikTok/YouTube) cujo público bate
  com o tema do jogo
- Lançamento coordenado: vários criadores postando na mesma janela de tempo
  gera pico de jogadores simultâneos, o que ajuda o algoritmo do Roblox a
  recomendar o jogo para mais gente
- Postagem consistente (ideal 1-2x/dia) em vez de posts esporádicos
- Comunidade no Discord para reter quem chegou pelo TikTok

## Estimativa de receita do Steal a Brainrot (para referência, não é exata)

As estimativas variam muito entre fontes (métodos de cálculo diferentes):
- ~US$ 1,4M/mês (uma fonte, confiança de 82%)
- ~US$ 11M/mês (outra fonte, período de pico)
- Um criador de conteúdo parceiro do jogo (KreekCraft) declarou ter
  ganhado pessoalmente mais de US$ 1M com o fenômeno (isso é receita dele
  como criador, não o dono/estúdio do jogo)

Não há um número oficial e confiável do quanto os desenvolvedores donos do
jogo embolsaram — os valores públicos citam receita da plataforma via
compras dentro do jogo, sujeita ao corte do Roblox (Roblox fica com boa
parte via DevEx/taxas de plataforma).

## Como vamos programar (workflow técnico)

- **Custo: R$ 0.** Roblox Studio é gratuito, Rojo é open-source e grátis,
  publicar no Roblox não custa nada.
- Escrever os scripts em Luau como arquivos de texto normais neste tipo de
  repositório
- Usar **Rojo** para sincronizar os arquivos locais com o Roblox Studio em
  tempo real (`rojo serve` + plugin Rojo dentro do Studio)

## Próximos passos em aberto

- [ ] Decidir: começar enxuto (plantar + 1-2 drones + loja) ou já incluir
      mutações/clima/PvP desde o início?
- [ ] Desenhar em detalhe o sistema de invasão/defesa dos drones
- [ ] Montar a estrutura inicial do projeto com Rojo
