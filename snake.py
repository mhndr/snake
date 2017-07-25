import curses

def init_curses():
	# get the curses screen window
	screen = curses.initscr()
 
	# turn off input echoing
	curses.noecho()
 
	# respond to keys immediately (don't wait for enter)
	curses.cbreak()

	# map arrow keys to special values
	screen.keypad(True)
	return screen

def print_grid():
	screen = init_curses()
	x = 0
	y = 0
	game_over = False
	try:
		height,width = screen.getmaxyx()
		screen.move(y,x)
		while True: 
			char = screen.getch()
			if char == ord('q'):
				break
			if game_over:
				screen.addstr(8,0,"Press 'q' to exit")
				continue
			#move the cursor
			if char == curses.KEY_RIGHT:
				if (x+1) < width:
					x = x + 1
			elif char == curses.KEY_LEFT:
				if (x-1) >= 0:
					x = x - 1
			elif char == curses.KEY_UP:
				if (y-1) >= 0:
					y = y - 1 
			elif char == curses.KEY_DOWN:
				if (y+1) < height:
					y = y + 1

			if char == curses.KEY_ENTER or char == 10 or char == 13:
				game_over = True
				screen.addstr(height/2,width/2,"Game Over.")
		
			screen.move(y,x)
	finally:
    	# shut down cleanly
		curses.nocbreak(); screen.keypad(0); curses.echo()
		curses.endwin()

if __name__ == '__main__':
	print_grid()


