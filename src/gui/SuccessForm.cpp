//---------------------------------------------------------------------------

#include <fmx.h>
#pragma hdrstop

#include "SuccessForm.h"
#include "PandaExpressForm.h"
#include "OptionsForm.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.fmx"
TMySuccessForm *MySuccessForm;
//---------------------------------------------------------------------------
__fastcall TMySuccessForm::TMySuccessForm(TComponent* Owner)
	: TForm(Owner)
{
}
//---------------------------------------------------------------------------
void __fastcall TMySuccessForm::BackButtonClick(TObject *Sender)
{
	this->Close();
}
//---------------------------------------------------------------------------
