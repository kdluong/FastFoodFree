//---------------------------------------------------------------------------

#ifndef FailFormH
#define FailFormH
//---------------------------------------------------------------------------
#include <System.Classes.hpp>
#include <FMX.Controls.hpp>
#include <FMX.Forms.hpp>
#include <FMX.Controls.Presentation.hpp>
#include <FMX.StdCtrls.hpp>
#include <FMX.Types.hpp>
//---------------------------------------------------------------------------
class TMyFailForm : public TForm
{
__published:	// IDE-managed Components
	TLabel *InfoLabel;
	TLabel *Label1;
	TButton *BackButton;
	void __fastcall BackButtonClick(TObject *Sender);
private:	// User declarations
public:		// User declarations
	__fastcall TMyFailForm(TComponent* Owner);
};
//---------------------------------------------------------------------------
extern PACKAGE TMyFailForm *MyFailForm;
//---------------------------------------------------------------------------
#endif
