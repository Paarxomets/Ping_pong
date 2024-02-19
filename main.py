import arcade
import pyfiglet 
bann=pyfiglet.figlet_format("pingpong", font='banner3-d')
print(bann)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_RADIUS = 10
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
MOVEMENT_SPEED = 5
BALL_SPEED = 5

class PongGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Ping Pong")
        arcade.set_background_color(arcade.color.BLACK)

        self.player1_score = 0
        self.player2_score = 0

        self.ball = arcade.SpriteCircle(BALL_RADIUS, arcade.color.WHITE)
        self.ball.center_x = width // 2
        self.ball.center_y = height // 2
        self.ball.change_x = BALL_SPEED
        self.ball.change_y = BALL_SPEED

        self.player1 = arcade.SpriteSolidColor(PADDLE_WIDTH, PADDLE_HEIGHT, arcade.color.WHITE)
        self.player1.center_x = PADDLE_WIDTH // 2
        self.player1.center_y = height // 2

        self.player2 = arcade.SpriteSolidColor(PADDLE_WIDTH, PADDLE_HEIGHT, arcade.color.WHITE)
        self.player2.center_x = width - PADDLE_WIDTH // 2
        self.player2.center_y = height // 2

    def on_draw(self):
        arcade.start_render()

        arcade.draw_text(f"Player 1 Score: {self.player1_score}", 20, SCREEN_HEIGHT - 40, arcade.color.WHITE, 16)
        arcade.draw_text(f"Player 2 Score: {self.player2_score}", SCREEN_WIDTH - 160, SCREEN_HEIGHT - 40, arcade.color.WHITE, 16)

        self.ball.draw()
        self.player1.draw()
        self.player2.draw()

    def update(self, delta_time):
        self.ball.center_x += self.ball.change_x
        self.ball.center_y += self.ball.change_y

        if self.ball.top >= SCREEN_HEIGHT or self.ball.bottom <= 0:
            self.ball.change_y *= -1

        if arcade.check_for_collision(self.ball, self.player1) or arcade.check_for_collision(self.ball, self.player2):
            self.ball.change_x *= -1

        if self.ball.right >= SCREEN_WIDTH:
            self.player1_score += 1
            self.ball.center_x = SCREEN_WIDTH // 2
            self.ball.center_y = SCREEN_HEIGHT // 2
            self.ball.change_x *= -1

        if self.ball.left <= 0:
            self.player2_score += 1
            self.ball.center_x = SCREEN_WIDTH // 2
            self.ball.center_y = SCREEN_HEIGHT // 2
            self.ball.change_x *= -1

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.player1.center_y += MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player1.center_y -= MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player2.center_y += MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player2.center_y -= MOVEMENT_SPEED

if __name__ == "__main__":
    game = PongGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
