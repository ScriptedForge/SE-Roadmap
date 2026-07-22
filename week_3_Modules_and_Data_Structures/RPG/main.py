## Importing data from other files ----------------------------------------
import players
import combat
import display
import economy

## Display and combat testing ---------------------------------------------
display.display_party_details(players.party)

combat.attack(players.knight, players.mage, 20)

display.display_party_details(players.party)