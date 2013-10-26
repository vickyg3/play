class Printer {

	static {
		isObjectCreated = false;
	}

	private static bool isObjectCreated;
	private static Printer p;

	public static getPrinter() {
		if (!isObjectCreated)
			p = new Printer;
		return p;
	}

	private Printer() {}
}


Printer p1 = Printer.getPrinter();
Printer p2 = Printer.getPrinter();
