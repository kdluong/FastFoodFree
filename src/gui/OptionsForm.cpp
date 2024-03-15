//---------------------------------------------------------------------------

#include <fmx.h>
#pragma hdrstop

#include "OptionsForm.h"
#include "HomeForm.h"
#include "PandaExpressForm.h"
#include "ComingSoonForm.h"
#include <memory>
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.fmx"
TMyOptionsForm *MyOptionsForm;
//---------------------------------------------------------------------------
__fastcall TMyOptionsForm::TMyOptionsForm(TComponent* Owner)
	: TForm(Owner)
{
}
//---------------------------------------------------------------------------
void __fastcall TMyOptionsForm::BackButtonClick(TObject *Sender)
{
	this->Close();
	MyHomeForm->Show();
}
//---------------------------------------------------------------------------
void __fastcall TMyOptionsForm::PandaExpressButtonClick(TObject *Sender)
{
	std::unique_ptr<TMyPandaExpressForm> pandaExpressForm(new TMyPandaExpressForm(NULL));
	pandaExpressForm->ShowModal();
}
//---------------------------------------------------------------------------
void __fastcall TMyOptionsForm::ChickFilAButtonClick(TObject *Sender)
{
	std::unique_ptr<TMyComingSoonForm> comingSoonForm(new TMyComingSoonForm(NULL));
	comingSoonForm->Label1->Text = "Sorry, Chick-fil-A surveys are not available at the moment.";
	comingSoonForm->ShowModal();
}
//---------------------------------------------------------------------------
void __fastcall TMyOptionsForm::JackInTheBoxButtonClick(TObject *Sender)
{
	std::unique_ptr<TMyComingSoonForm> comingSoonForm(new TMyComingSoonForm(NULL));
	comingSoonForm->Label1->Text = "Sorry, Jack in the Box surveys are not available at the moment.";
	comingSoonForm->ShowModal();
}
//---------------------------------------------------------------------------
void __fastcall TMyOptionsForm::McDonaldsButtonClick(TObject *Sender)
{
	std::unique_ptr<TMyComingSoonForm> comingSoonForm(new TMyComingSoonForm(NULL));
	comingSoonForm->Label1->Text = "Sorry, McDonald's surveys are not available at the moment.";
	comingSoonForm->ShowModal();
}
//---------------------------------------------------------------------------
void __fastcall TMyOptionsForm::PaneraBreadButtonClick(TObject *Sender)
{
	std::unique_ptr<TMyComingSoonForm> comingSoonForm(new TMyComingSoonForm(NULL));
	comingSoonForm->Label1->Text = "Sorry, Panera Bread surveys are not available at the moment.";
	comingSoonForm->ShowModal();
}
//---------------------------------------------------------------------------

