
# Contributing to Loteria Game

## Current Status

The base code for the Loteria game is complete. Below are the next steps and areas where contributions are needed:

### Art for Cards
- Finish the artwork for the cards. Currently, 7 out of 54 cards are done. Please refer to `cardslist.txt` for the list of cards.

### Error Handling and Code Hardening
- Ensure that players cannot use the same name.
- After a game ends, all players should be returned to the first screen, and the game number should become available again.
- Prepare the code for deployment on a public server. Address any security and functionality concerns.
- Ensure that if a browser is refreshed and the game is in session, the game remains active.

### Visual Design Improvements
- Update the board to have a background that makes all choices look like they are on an actual Loteria board.
- Improve the font and background design.
- Instead of highlighting red, drop a token (a coin or a pebble) to mark a spot.
- Add animation for drawing a card.
- Modernize the layout, background, buttons, fonts, etc.

### Testing
- Test with multiple players, including handling tied games.
- Ensure that all edge cases are covered and the game behaves as expected.

## How to Contribute

1. **Fork the repository**: Click on the "Fork" button at the top of the repository page to create a copy of the repository in your account.

2. **Clone your fork**: Clone your forked repository to your local machine using the following command:
   \`\`\`bash
   git clone https://github.com/yourusername/loteria-game.git
   cd loteria-game
   \`\`\`

3. **Create a branch**: Create a new branch for your work:
   \`\`\`bash
   git checkout -b your-feature-branch
   \`\`\`

4. **Make your changes**: Implement your changes or new features.

5. **Test your changes**: Ensure that your changes work as expected and do not break existing functionality.

6. **Commit your changes**: Commit your changes with a descriptive commit message:
   \`\`\`bash
   git add .
   git commit -m "Description of your changes"
   \`\`\`

7. **Push to your fork**: Push your changes to your forked repository:
   \`\`\`bash
   git push origin your-feature-branch
   \`\`\`

8. **Create a Pull Request**: Go to the original repository and create a pull request from your fork. Provide a clear description of your changes and any related issue numbers.

## Contribution Guidelines

- Follow the coding style and conventions used in the project.
- Ensure that your code is well-documented.
- Write tests for new functionality.
- Be respectful and considerate in your communications.

Thank you for your contributions!

---

Enjoy contributing and happy coding!

