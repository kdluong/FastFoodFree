//---------------------------------------------------------------------------

#include <fmx.h>
#pragma hdrstop

#include "HomeForm.h"
#include "OptionsForm.h"
#include <memory>
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.fmx"
TMyHomeForm *MyHomeForm;
//---------------------------------------------------------------------------
__fastcall TMyHomeForm::TMyHomeForm(TComponent* Owner)
	: TForm(Owner)
{
}
//---------------------------------------------------------------------------
void __fastcall TMyHomeForm::StartButtonClick(TObject *Sender)
{
	this->Hide();
	std::unique_ptr<TMyOptionsForm> optionForm(new TMyOptionsForm(NULL));
	optionForm->ShowModal();
}
//---------------------------------------------------------------------------

