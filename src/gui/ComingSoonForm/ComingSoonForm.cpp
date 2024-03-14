//---------------------------------------------------------------------------

#include <fmx.h>
#pragma hdrstop

#include "ComingSoonForm.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.fmx"
TMyComingSoonForm *MyComingSoonForm;
//---------------------------------------------------------------------------
__fastcall TMyComingSoonForm::TMyComingSoonForm(TComponent* Owner)
	: TForm(Owner)
{
}
//---------------------------------------------------------------------------
void __fastcall TMyComingSoonForm::BackButtonClick(TObject *Sender)
{
	this->Close();
}
//---------------------------------------------------------------------------
