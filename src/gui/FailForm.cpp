//---------------------------------------------------------------------------

#include <fmx.h>
#pragma hdrstop

#include "FailForm.h"
#include "PandaExpressForm.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.fmx"
TMyFailForm *MyFailForm;
//---------------------------------------------------------------------------
__fastcall TMyFailForm::TMyFailForm(TComponent* Owner)
	: TForm(Owner)
{
}
//---------------------------------------------------------------------------
void __fastcall TMyFailForm::BackButtonClick(TObject *Sender)
{
	this->Close();
}
//---------------------------------------------------------------------------
