/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     | Website:  https://openfoam.org
    \\  /    A nd           | Copyright (C) 2011-2019 OpenFOAM Foundation
     \\/     M anipulation  |
-------------------------------------------------------------------------------
License
    This file is part of OpenFOAM.

    OpenFOAM is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    OpenFOAM is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
    for more details.

    You should have received a copy of the GNU General Public License
    along with OpenFOAM.  If not, see <http://www.gnu.org/licenses/>.

\*---------------------------------------------------------------------------*/

#include "blastRadiationModel.H"
#include "volFields.H"

// * * * * * * * * * * * * * * * * Constructors  * * * * * * * * * * * * * * //

Foam::autoPtr<Foam::blastRadiationModel> Foam::blastRadiationModel::New
(
    const volScalarField& T
)
{
    IOobject radIO
    (
        "radiationProperties",
        T.time().constant(),
        T.mesh(),
        IOobject::MUST_READ_IF_MODIFIED,
        IOobject::NO_WRITE,
        false
    );

    word modelType("none");
    if (radIO.typeHeaderOk<IOdictionary>(false))
    {
        IOdictionary(radIO).lookup("radiationModel") >> modelType;
    }
    else
    {
        Info<< "Radiation model not active: radiationProperties not found"
            << endl;
    }

    Info<< "Selecting radiationModel " << modelType << endl;

    TConstructorTable::iterator cstrIter =
        TConstructorTablePtr_->find(modelType);

    if (cstrIter == TConstructorTablePtr_->end())
    {
        FatalErrorInFunction
            << "Unknown blastRadiationModel type "
            << modelType << nl << nl
            << "Valid blastRadiationModel types are:" << nl
            << TConstructorTablePtr_->sortedToc()
            << exit(FatalError);
    }

    return autoPtr<blastRadiationModel>(cstrIter()(T));
}


Foam::autoPtr<Foam::blastRadiationModel> Foam::blastRadiationModel::New
(
    const dictionary& dict,
    const volScalarField& T
)
{
    const word modelType(dict.lookup<word>("blastRadiationModel"));

    Info<< "Selecting blastRadiationModel " << modelType << endl;

    dictionaryConstructorTable::iterator cstrIter =
        dictionaryConstructorTablePtr_->find(modelType);

    if (cstrIter == dictionaryConstructorTablePtr_->end())
    {
        FatalErrorInFunction
            << "Unknown blastRadiationModel type "
            << modelType << nl << nl
            << "Valid blastRadiationModel types are:" << nl
            << dictionaryConstructorTablePtr_->sortedToc()
            << exit(FatalError);
    }

    return autoPtr<blastRadiationModel>(cstrIter()(dict, T));
}


// ************************************************************************* //
