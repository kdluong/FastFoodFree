//---------------------------------------------------------------------------

#ifndef OptionsFormH
#define OptionsFormH
//---------------------------------------------------------------------------
#include <System.Classes.hpp>
#include <FMX.Controls.hpp>
#include <FMX.Forms.hpp>
#include <FMX.Controls.Presentation.hpp>
#include <FMX.StdCtrls.hpp>
#include <FMX.Types.hpp>
//---------------------------------------------------------------------------
class TMyOptionsForm : public TForm
{
__published:	// IDE-managed Components
	TLabel *SelectLabel;
	TButton *ChickFilAButton;
	TButton *JackInTheBoxButton;
	TButton *McDonaldsButton;
	TButton *PandaExpressButton;
	TButton *PaneraBreadButton;
	TButton *BackButton;
	void __fastcall BackButtonClick(TObject *Sender);
	void __fastcall PandaExpressButtonClick(TObject *Sender);
	void __fastcall ChickFilAButtonClick(TObject *Sender);
	void __fastcall JackInTheBoxButtonClick(TObject *Sender);
	void __fastcall McDonaldsButtonClick(TObject *Sender);
	void __fastcall PaneraBreadButtonClick(TObject *Sender);
private:	// User declarations
public:		// User declarations
	__fastcall TMyOptionsForm(TComponent* Owner);
};
//---------------------------------------------------------------------------
extern PACKAGE TMyOptionsForm *MyOptionsForm;
//---------------------------------------------------------------------------
#endif
