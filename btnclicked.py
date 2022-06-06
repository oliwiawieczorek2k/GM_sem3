	def button_clicked(self):
		print("clicked")
		pts = create_points(10)
		hull = graham_scan(pts,False)
		self.label.setText("Punkty: "+str(pts)+"\nOtoczka: "+str(hull))
		self.widget.set
		scatter_plot(pts,hull)