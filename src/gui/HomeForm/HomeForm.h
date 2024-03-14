//---------------------------------------------------------------------------

#ifndef HomeFormH
#define HomeFormH
//---------------------------------------------------------------------------
#include <System.Classes.hpp>
#include <FMX.Controls.hpp>
#include <FMX.Forms.hpp>
#include <FMX.Controls.Presentation.hpp>
#include <FMX.StdCtrls.hpp>
#include <FMX.Types.hpp>
#include <FMX.Colors.hpp>
#include <FMX.ExtCtrls.hpp>
#include <FMX.Layouts.hpp>
#include <FMX.Controls3D.hpp>
#include <FMX.Objects3D.hpp>
#include <System.Math.Vectors.hpp>
#include <FMX.TabControl.hpp>
#include <FMX.WebBrowser.hpp>
#include <Datasnap.DSCommonServer.hpp>
#include <Datasnap.DSHTTP.hpp>
#include <Datasnap.DSHTTPWebBroker.hpp>
#include <IPPeerServer.hpp>
//---------------------------------------------------------------------------
class TMyHomeForm : public TForm
{
__published:	// IDE-managed Components
	TButton *StartButton;
	TLabel *FastLabel;
	TLabel *FoodLabel;
	TLabel *FreeLabel;
	void __fastcall StartButtonClick(TObject *Sender);
private:	// User declarations
public:		// User declarations
	__fastcall TMyHomeForm(TComponent* Owner);
};
//---------------------------------------------------------------------------
extern PACKAGE TMyHomeForm *MyHomeForm;
//---------------------------------------------------------------------------
#endif
