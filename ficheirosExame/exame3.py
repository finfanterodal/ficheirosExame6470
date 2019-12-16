import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class Exame(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exame 16-12-2019")
        self.set_border_width(10)

        solapas = Gtk.Notebook()

        self.add(solapas)
        self.gridUI = Gtk.Grid()
        self.solapa1 = Gtk.Grid()
        self.solapa1.set_column_spacing(6)
        self.solapa1.set_border_width(5)
        solapas.append_page(self.gridUI, Gtk.Label('Zoa 1'))

        lblTitulo = Gtk.Label("Configuración zoa de rego")
        lblActivada = Gtk.Label("Activada")
        lblHoraComezo = Gtk.Label("Hora de comezo")
        lblDuracionRego = Gtk.Label("Duración do Rego")

        swtActivada = Gtk.Switch()
        txtHoraComezo = Gtk.Entry()
        cmbDuracionRego = Gtk.ComboBox()
        btnAceptar = Gtk.Button("Aceptar")

        # CONTROL DE SEÑAL SWITCH
        swtActivada.connect("notify::active", self.on_switch_activated)

        # Asignacion ComboBox
        lista_formatos = Gtk.ListStore(str)
        lista_formatos.append(["5 min"])
        lista_formatos.append(["10 min"])
        lista_formatos.append(["20 min"])
        lista_formatos.append(["30 min"])
        lista_formatos.append(["60 min"])
        cmbDuracionRego.set_model(lista_formatos)
        celdaTexto = Gtk.CellRendererText()  # cada parte del combo es un cell text
        cmbDuracionRego.pack_start(celdaTexto, True)  # añadimos la celda
        cmbDuracionRego.add_attribute(celdaTexto, "text",
                                      0)

        frmOpcions = Gtk.Frame(label="Opcións")
        caixaH1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        chkAntixiada = Gtk.CheckButton("Antixiada")
        chkDiario = Gtk.CheckButton("Diario")
        chkChuvia = Gtk.CheckButton("Chuvia")
        caixaH1.pack_start(chkAntixiada, True, True, 0)
        caixaH1.pack_start(chkChuvia, True, True, 0)
        caixaH1.pack_end(chkDiario, True, True, 0)

        # BLOQUEO DE CHECKBUTTONS
        chkDiario.connect("toggled", self.on_chkDiario_toggled)

        frmOpcions.add(caixaH1)

        builder = Gtk.Builder()
        builder.add_from_file("./cadroDiasGlade.glade")
        cadro = builder.get_object("frame1")
        self.chkLuns = builder.get_object("chkLuns")
        self.chkMartes = builder.get_object("chkMartes")
        self.chkMercores = builder.get_object("chkMercores")
        self.chkXoves = builder.get_object("chkXoves")
        self.chkVenres = builder.get_object("chkVenres")
        self.chkSabado = builder.get_object("chkSabado")
        self.chkDomingo = builder.get_object("chkDomingo")

        caixaV1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        caixaV1.pack_start(cadro, True, True, 0)
        caixaV1.pack_end(btnAceptar, True, True, 0)

        self.solapa1.add(lblTitulo)
        self.solapa1.attach_next_to(lblActivada, lblTitulo, Gtk.PositionType.BOTTOM, 1, 1)
        self.solapa1.attach_next_to(swtActivada, lblActivada, Gtk.PositionType.RIGHT, 1, 1)
        self.solapa1.attach_next_to(lblHoraComezo, lblActivada, Gtk.PositionType.BOTTOM, 1, 1)
        self.solapa1.attach_next_to(txtHoraComezo, lblHoraComezo, Gtk.PositionType.RIGHT, 1, 1)
        self.solapa1.attach_next_to(lblDuracionRego, lblHoraComezo, Gtk.PositionType.BOTTOM, 1, 1)
        self.solapa1.attach_next_to(cmbDuracionRego, lblDuracionRego, Gtk.PositionType.RIGHT, 1, 1)

        self.gridUI.add(self.solapa1)
        self.gridUI.attach_next_to(frmOpcions, self.solapa1, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridUI.attach_next_to(caixaV1, self.solapa1, Gtk.PositionType.RIGHT, 1, 2)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_switch_activated(self, switch, gparam):
        if switch.get_active():
            state = "on"
        else:
            state = "off"

        print("Switch en estado", state)

    def on_chkDiario_toggled(self, control):
        if control.get_active():
            print("SELECCIONADO")
            self.chkLuns.set_sensitive(False)
            #self.chkMartes.set_sensitive(False)
            #self.chkMercores.set_sensitive(False)
            #self.chkXoves.set_sensitive(False)
            #self.chkVenres.set_sensitive(False)
            #self.chkSabado.set_sensitive(False)
            #self.chkDomingo.set_sensitive(False)
        else:
            print("DESSELECIONADO")
            self.chkLuns.set_sensitive(True)
            #self.chkMartes.set_sensitive(True)
            #self.chkMercores.set_sensitive(True)
            #self.chkXoves.set_sensitive(True)
            #self.chkVenres.set_sensitive(True)
            #self.chkSabado.set_sensitive(True)
            #self.chkDomingo.set_sensitive(True)


if __name__ == "__main__":
    Exame()
    Gtk.main()
